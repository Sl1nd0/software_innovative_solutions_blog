import json
from .models import Users
from datetime import datetime

def user_login_query(user): 

	result = {"success": False, "result": {}, "error": []}

	try:            
		email = user['email']
		password = user['password']
		user_login_result = Users.objects.filter(user_name=email, password=password).values().first()
		
		print("user_login_result")
		print(user_login_result)

		if user_login_result is None:
			result["error"].append("User {0} not found, please check if your username and password are correct" .format(email))	
			return result
		else:
			result["success"] = True
			result["result"] = user_login_result
			result["error"] = []
			return result
		return result

	except Exception as error:
			result["success"] = False
			result["result"] = user
			result["error"].append(error)	
	return result

def get_user_by_id_query(user): 

	result = {"success": False, "result": {}, "error": []}

	try:    
		print(user["id"])
		user_query_result = Users.objects.filter(id=user["id"]).values().first()

		if user_query_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = user_query_result
			result["error"] = None
			return result
		return result

	except Exception as error:
			print("get_user_by_id_query error")
			print(error)
			result["success"] = False
			result["result"] = user
			result["error"].append(error)	
	return result