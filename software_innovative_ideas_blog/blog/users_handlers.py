import json
from .models import Users
from .models import UserRoles
from datetime import datetime
from . import user_roles_handlers

def add_user(user): 
    
    result = {"success": False, "result": None, "error": []}

    try:            

           date = datetime.now();

           #add user to a role
           if user['email'] == "ssankabi@gmail.com":
            role = UserRoles.objects.filter(role="administrator").first()
           else:
            role = UserRoles.objects.filter(role="user").first()

           user_entity = Users(user_name = user['user_name'], surname = user['surname'], name = user['name'], 
                                email = user['email'], identifier = user['identifier'], password = user['password'], birthdate = user['birthdate'], 
                                cell_number = user['cell_number'], User_roleID = role, user_date = date)
           
           user_entity.save()

           if user_entity.pk > 0:
            result["success"] = True
            result["result"] = Users.objects.filter(email= user['email']).values().first()
            result["error"] = []
            return result
           return result

    except Exception as error:
            print("add_user error")
            print(error)
            result["success"] = False
            result["result"] = user
            result["error"].append(error)
    return result