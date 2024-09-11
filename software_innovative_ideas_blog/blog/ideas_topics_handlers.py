import json
from .models import IdeasTopics
from datetime import datetime

def add_idea_topic(model): 

    result = {"success": False, "result": None, "error": []}

    print("add_idea_topic")
    
    try:
           print(model)
           print(model["ideaID"].pk)
           print(model["topicID"].pk)
           print("TEST")
           ideas_topics_query_result = IdeasTopics.objects.filter(ideaID=model["ideaID"].pk, topicID=model["topicID"].pk).values().first()
           print("ideas_topics_query_result") 

           if ideas_topics_query_result != None:
            result["success"] = False
            result["result"] = model
            result["error"].append("ideaID {0}, topicID {1} combo already exists in the IdeasTopics table" .format(model["ideaID"], model["topicID"]))  
            return result

           ideas_topics_entity = IdeasTopics(topicID = model["topicID"], ideaID = model["ideaID"])
           
           ideas_topics_entity.save()

           print("ideas_topics_entity")
           print(ideas_topics_entity)

           if ideas_topics_entity.pk > 0:
            result["success"] = True
            result["result"] = model
            result["error"] = []
            return result;
           return result

    except Exception as error:
            print("add_idea_topic error")
            print(error)
            result["success"] = False
            result["result"] = model
            result["error"].append(error)
    return result