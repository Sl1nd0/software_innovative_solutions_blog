import json
from .models import idea
from datetime import datetime
from . import users_queries
from . import ideas_topics_handlers
from . import topics_queries

def add_idea(idea): 

    result = {"success": False, "result": None, "Error": []}

    try:       
           user = users_queries.get_user_by_id_query(idea["userID"]);
           
           topic_dto = {
               "id": idea["topicID"]
           }

           topic = topics_queries.list_topics_by_id_query(topic_dto);
           
           if user is None:
            result["success"] = False
            result["result"] = user
            result["Error"] = "User doesn't exist for id {0}" .format(idea["userID"]))
           return result;

           date = datetime.now();

           idea_entity = Ideas(userID = user["id"], idea = idea["idea"] idea_date = date)
        
           idea_entity.save()

           #link idea and topic
           model = {
               "ideaID": idea["topicID"],
               "topicID": idea_entity.pk
           }

           ideas_topics_handlers_result = ideas_topics_handlers.add_idea_topic(model)

           result["Error"].append(ideas_topics_handlers_result["Error"])

           if idea_entity.pk > 0:
            result["success"] = True
            result["result"] = user
            result["Error"] = None
           return result;

    except Exception as error:
            result["success"] = False
            result["result"] = user
            result["Error"].append(error)
    return result