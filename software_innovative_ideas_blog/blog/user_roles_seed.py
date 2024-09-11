from . import user_roles_handlers
from .models import UserRoles

def user_roles_seed():
	
	try:
		
		roles = UserRoles.objects.values()

		result = {"success": False, "result": None, "error": []}

		if len(roles) > 0:
			result["success"] = True
			result["result"] = roles
			return result
		
		role = {
			"role" : "administrator"
		}

		addroleresult = user_roles_handlers.add_user_role(role)

		if addroleresult["success"] == True:
			print("{0} role has been added successfully" .format(role["role"]))
		
		result["success"] = True

		role = {
			"role" : "user"
		}

		addroleresult = user_roles_handlers.add_user_role(role)

		print("{0} role has been added successfully" .format(role["role"]))

		result["success"] = True

	except Exception as error:
		print("user_roles_seed error")
		print(error)
		result["success"] = False
		result["result"] = UserRoles.objects.values()
		result["error"].append(error)
	return result