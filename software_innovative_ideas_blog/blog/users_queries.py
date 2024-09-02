import json
from .models import Users
from datetime import datetime

def user_login_query(user): 

	result = {"success": False, "result": {}, "error": []}

	try:            
		email = user['email']
		password = user['password']
		user_login_result = Users.objects.filter(username=email, password=password).values()
	
		if user_login_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = user_login_result
			result["error"] = []
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = user
			result["error"].append(error)	
	return result

def get_user_by_id_query(user): 

	result = {"success": False, "result": {}, "error": []}

	try:           
		user_query_result = Users.objects.filter(id=user["id"]).values()
	
		if user_query_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = user_query_result
			result["error"] = None
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = user
			result["error"].append(error)	
	return result