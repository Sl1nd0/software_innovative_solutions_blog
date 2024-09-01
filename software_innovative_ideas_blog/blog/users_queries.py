import json
from .models import Users
from datetime import datetime

def user_login_query(user): 

	result = {"success": False, "result": {}, "Error": []}

	try:            
		email = user['email']
		password = user['password']
		user_login_result = Users.objects.filter(username=email, password=password).values()
	
		if user_login_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = user_login_result
			result["Error"] = None
		return result

	except Exception as error:
			result["success"] = True
			result["result"] = user
			result["Error"].append(error)	
	return result