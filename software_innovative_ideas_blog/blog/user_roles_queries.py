import json
from .models import UserRoles
from datetime import datetime

def get_user_role_by_id_query(roleid): 

	result = {"success": False, "result": {}, "error": []}

	try:     
	
		user_role_result = UserRoles.objects.filter(id=roleid).values().first()
		
		print("user_role")
		print(user_role_result)

		if user_role_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = user_role_result
			result["error"] = []
			return result
		return result

	except Exception as error:
			print("get_user_role_by_id_query error")
			print(error)
			result["success"] = False
			result["result"] = roleid
			result["error"].append("role doesn't exist for role_id {0}" .format(roleid))
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

	except Exception as error:
			print("get_user_by_id_query error")
			print(error)
			result["success"] = False
			result["result"] = user
			result["error"].append(error)	
	return result