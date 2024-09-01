import json
from .models import Topics
from datetime import datetime

def add_topic(topic): 

    result = {"success": False, "result": None, "Error": []}

    try:
           date = datetime.now();

           topic_entity = Topics(topic = topic["topic"], topic_date= date)
    
           topic_entity.save()

           if topic_entity.pk > 0:
            result["success"] = True
            result["result"] = user
            result["Error"] = None
           return result;

    except Exception as error:
            result["success"] = False
            result["result"] = user
            result["Error"].append(error)
    return result