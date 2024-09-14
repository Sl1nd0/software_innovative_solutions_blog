import traceback
import json
from .models import Ideas
from .models import IdeasTopics
from .models import Users
from .models import Topics
from .models import Comments
from .models import Likes
from datetime import datetime
from . import users_queries
from . import ideas_topics_handlers
from . import topics_queries

def add_idea(idea): 
    print("#idea")
    print(idea)
    result = {"success": False, "result": None, "error": []}

    try:       
           user_dto = {
           "id" : idea["userID"]
           }

           user_query = Users.objects.filter(id = idea["userID"]).first()

           if user_query is None:
            result["success"] = False
            result["result"] = user_query
            result["error"] = "User doesn't exist for id {0}" .format(idea["userID"])
            return result;

           topic_dto = {
               "id": idea["topicID"]
           }

           topic = topics_queries.list_topics_by_id_query(topic_dto)

           if topic is None:
            result["success"] = False
            result["result"] = topic
            result["error"] = "topic doesn't exist for id {0}" .format(topic_dto["id"])
            return result;

           date = datetime.now();

           idea_entity = Ideas(userID = user_query, idea = idea["idea"], idea_date = date)
           
           idea_entity.save()

           #link idea and topic
           model = {
               "ideaID":  idea_entity,
               "topicID": Topics.objects.filter(id = idea["topicID"]).first()
           }

           ideas_topics_handlers_result = ideas_topics_handlers.add_idea_topic(model)

           if ideas_topics_handlers_result["success"] == True:
            result["success"] = True
            result["result"] = ideas_topics_handlers_result
            result["error"] = None
            return result;

           result["error"].append(ideas_topics_handlers_result["error"])

           if idea_entity.pk > 0:
            result["success"] = True
            result["result"] = ideas_topics_handlers_result
            result["error"] = None
            return result;

           return result;

    except Exception as error:
            print("add_idea error")
            stack_trace = traceback.format_exc()
            print(stack_trace)
            print(error)
            result["success"] = False
            result["result"] = idea
            result["error"].append(error)
    return result

def edit_idea(idea): 

    print("#edit_idea idea")
    print(idea)
    result = {"success": False, "result": None, "error": []}

    try:    
           topic = Topics.objects.get(id = idea["topicID"])

           if topic is None:
            result["success"] = False
            result["result"] = topic
            result["error"] = "topic doesn't exist for id {0}" .format(idea["topicID"])
            return result;

           date = datetime.now();

           idea_entity = Ideas.objects.get(id = idea["ideaID"])
           
           if idea_entity == None:
            result["success"] = False
            result["result"] = idea
            result["error"].append("Idea doesn't exist for idea id {0}" .format(idea["ideaID"]))
            return result;

           ideas_topics_entity = IdeasTopics.objects.get(ideaID=idea["ideaID"])
           
           if ideas_topics_entity == None:
            result["success"] = False
            result["result"] = idea
            result["error"].append("IdeaTopic record doesn't exist for idea id {0}'" .format(idea["ideaID"]))
            return result;

           idea_entity.idea = idea["idea"]
           idea_entity.save()

           ideas_topics_entity.topicID = topic
           ideas_topics_entity.save()
           
           if idea_entity.idea == idea["idea"]:
            result["success"] = True
            result["result"] = idea_entity
            result["error"] = None
            return result;

           return result;

    except Exception as error:
            print("edit_idea error")
            stack_trace = traceback.format_exc()
            print(stack_trace)
            print(error)
            result["success"] = False
            result["result"] = idea
            result["error"].append(error)
    return result

def delete_idea(idea): 
    print("#delete_idea idea")
    print(idea)
    result = {"success": False, "result": None, "error": []}

    try:  
         
          idea_comments_entity = Comments.objects.get(ideaID = idea["ideaID"])
          if idea_comments_entity != None:
           idea_comments_entity.delete()

          idea_likes_entity = Likes.objects.get(ideaID = idea["ideaID"])
          if idea_comments_entity != None:
           idea_likes_entity.delete()

          idea_topic_entity = IdeasTopics.objects.get(ideaID = idea["ideaID"])
          
          print("delete_idea idea_entity")
          print(idea_topic_entity)

          if idea_topic_entity == None:
           result["success"] = False
           result["result"] = idea
           result["error"].append("IdeasTopic for Idea {0}, doesn't exist" .format(idea["ideaID"]))
           return result

          idea_topic_entity.delete()

          idea_entity = Ideas.objects.get(id=idea["ideaID"])

          if idea_entity == None:
           result["success"] = False
           result["result"] = idea
           result["error"].append("Idea {0} doesn't exist" .format(idea["ideaID"]))
           return result

          idea_entity.delete()

          idea_entity = Ideas.objects.filter(id=idea["ideaID"]).first()
          print("delete_idea idea_entity")
          print(idea_entity)

          if idea_entity == None:
           result["success"] = True
           result["result"] = idea
           result["error"] = []
           return result
          return result

    except Exception as error:
            print("delete_idea error")
            stack_trace = traceback.format_exc()
            print(stack_trace)
            print(error)
            result["success"] = False
            result["result"] = idea
            result["error"].append(error)
    return result