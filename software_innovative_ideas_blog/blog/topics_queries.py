import json
from .models import Topics
from datetime import datetime

def list_topics_by_id_query(topic): 

	result = {"success": False, "result": {}, "Error": []}

	try: 

		list_topics_query_result = Topics.objects.filter(id=topic["id"]).values()
		
		if list_topics_query_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = list_topics_query_result
			result["Error"] = []
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = topic
			result["Error"].append(error)	
	return result

def get_topic_by_id_query(id): 

	result = {"success": False, "result": {}, "Error": []}

	try: 

		get_topic_query_result = Topics.objects.filter(id=id).values().first()
		
		print(get_topic_query_result["topic"])

		if get_topic_query_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = get_topic_query_result
			result["Error"] = []
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = id
			result["Error"].append(error)	
	return result

def list_topics_query(): 

	result = {"success": False, "result": {}, "Error": []}

	try: 

		list_topics_query_result = Topics.objects.values()
		
		if list_topics_query_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = list_topics_query_result
			result["Error"] = []
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = {}
			result["Error"].append(error)	
	return result