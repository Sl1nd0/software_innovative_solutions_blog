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
           return result;

    except Exception as error:
            print(error)
            result["success"] = False
            result["result"] = topic
            result["error"].append(error)
    return result