import json
import django
from django.conf import settings
from .models import UserRoles
from datetime import datetime

def add_user_role(role): 
    
    result = {"success": False, "result": None, "error": []}
    
    try:      
           date = datetime.now();

           user_roles_entity = UserRoles(role=role["role"], role_date = date)
           
           user_roles_entity.save()
           
           if user_roles_entity.pk > 0:
            result["success"] = True
            result["result"] = UserRoles.objects.filter(role=role["role"]).values()
            result["error"] = []
            return result
           return result

    except Exception as error:
           print("add_user_role error")
           print(error)
           result["success"] = False
           result["result"] = role
           result["error"].append(error)
    return result