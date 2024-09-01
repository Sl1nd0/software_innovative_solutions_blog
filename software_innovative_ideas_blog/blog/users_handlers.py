import json
from .models import Users
from datetime import datetime

def add_user(user): 

    result = {"success": False, "result": None, "Error": []}

    try:            

           date = datetime.now();

           user_entity = Users(user_name = user['email'], surname = user['surname'], name = user['name'], 
                                email = user['email'], identifier = user['identifier'], password = user['password'], birthdate = user['birthdate'], 
                                cell_number = user['cell_number'], user_date = date)
    
           user_entity.save()

           if user_entity.pk > 0:
            result["success"] = True
            result["result"] = user
            result["Error"] = None
           return result;

    except Exception as error:
            result["success"] = False
            result["result"] = user
            result["Error"].append(error)
    return result