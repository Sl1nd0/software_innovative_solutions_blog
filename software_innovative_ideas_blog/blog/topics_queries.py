import json
from .models import Topics
from .models import IdeasTopics
from datetime import datetime

def list_topics_by_id_query(topic): 
	print("#topic")
	print(topic)
	result = {"success": False, "result": {}, "error": []}

	try: 

		list_topics_query_result = Topics.objects.filter(id=topic["id"]).values()
		print(list_topics_query_result)
		if list_topics_query_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = list_topics_query_result
			result["error"] = []
			return result
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = topic
			result["error"].append(error)	
	return result

def get_topic_by_id_query(id): 

	result = {"success": False, "result": {}, "error": []}

	try: 

		get_topic_query_result = Topics.objects.filter(id=id).values().first()
		
		print(get_topic_query_result["topic"])

		if get_topic_query_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = get_topic_query_result
			result["error"] = []
			return result
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = id
			result["error"].append(error)	
	return result

def list_topics_query(): 

	result = {"success": False, "result": {}, "error": []}

	try: 

		list_topics_query_result = Topics.objects.values().distinct()
		
		if list_topics_query_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = list_topics_query_result
			result["error"] = []
			return result
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = {}
			result["error"].append(error)	
	return result
