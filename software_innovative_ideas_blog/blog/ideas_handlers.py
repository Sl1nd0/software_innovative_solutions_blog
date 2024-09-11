import traceback
import json
from .models import Ideas
from .models import Users
from .models import Topics
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
               "topicID": Topics.object.filter(id = idea["topicID"]).first()
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