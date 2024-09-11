import json
from .models import Topics
from datetime import datetime

def add_topic(topic): 

    result = {"success": False, "result": None, "error": []}

    try:
           date = datetime.now();

           topic_entity = Topics(topic = topic["topic"], topic_date= date)
    
           topic_entity.save()

           if topic_entity.pk > 0:
            result["success"] = True
            result["result"] = topic
            result["error"] = []
            return result
           return result

    except Exception as error:
            print(error)
            result["success"] = False
            result["result"] = topic
            result["error"].append(error)
    return result

def edit_topic(topic): 

    result = {"success": False, "result": None, "error": []}

    try:
           topic_entity = Topics.objects.get(id=topic["id"])
           print(topic["topic"])

           topic_entity.topic = topic["topic"]

           topic_entity.save()

           result["success"] = True
           result["result"] = Topics.objects.filter(id=topic["id"]).values().first()
           result["error"] = []
           return result;

    except Exception as error:
            print("edit_topic error")
            print(error)
            result["success"] = False
            result["result"] = topic
            result["error"].append(error)
    return result

def delete_topic(id): 

    result = {"success": False, "result": None, "error": []}

    try:
           topic_entity = Topics.objects.get(id=id)

           topic_entity.delete()    
            
           result["success"] = True
           result["result"] = id
           result["error"] = []
           return result

    except Exception as error:
            print(error)
            result["success"] = False
            result["result"] = id
            result["error"].append(error)
    return result