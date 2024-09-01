import json
from .models import IdeasTopics
from datetime import datetime

def add_idea_topic(model): 

    result = {"success": False, "result": None, "Error": []}

    try:
           ideas_topics_query_result = IdeasTopics.objects.filter(ideaID=model["ideaID"], topicID=model["topicID"]).values()

           if ideas_topics_query_result != None
            result["success"] = False
            result["result"] = model
            result["Error"].append("ideaID {0}, topicID {1} combo already exists in the IdeasTopics table" .format(model["ideaID"], model["topicID"]))  
           return result

           ideas_topics_entity = IdeasTopics(topicID = model["topicID"], ideaID = model["ideaID"])
    
           ideas_topics_entity.save()

           if ideas_topics_entity.pk > 0:
            result["success"] = True
            result["result"] = user
            result["Error"] = None
           return result;

    except Exception as error:
            result["success"] = False
            result["result"] = user
            result["Error"].append(error)
    return result