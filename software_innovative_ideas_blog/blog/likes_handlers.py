import json
import django
from django.conf import settings
from .models import Likes
from .models import Ideas
from .models import Users
from datetime import datetime

def add_like(like_dto): 
    
    result = {"success": False, "result": None, "error": []}
    
    try:     
           print(like_dto)
           date = datetime.now();
           deleted = False
           like_result = Likes.objects.all().filter(userID = like_dto["userID"], ideaID = like_dto["ideaID"]).first()
           
           print("liked")
           if like_result != None:
            print("liked")
            deleted = True
            liked = Likes.objects.get(userID =like_dto["userID"], ideaID = like_dto["ideaID"])
            liked.delete()   
            
           if deleted == True:
            return result

           user = Users.objects.filter(id=like_dto["userID"]).first()
           print("#user")
           print(user)

           if user is None:
            result["success"] = False
            result["result"] = like_dto
            result["error"].append("user doesn't exist for " .format(like_dto["userID"]))
            return result

           idea = Ideas.objects.filter(id=like_dto["ideaID"]).first()
           print("#idea")
           print(idea)

           if idea is None:
            result["success"] = False
            result["result"] = like_dto
            result["error"].append("Idea doesn't exist for {0}" .format(like_dto["ideaID"]))
            return result

           likes_entity = Likes(userID = user, ideaID = idea, like_date = date)
           
           likes_entity.save()
           print("#likes_entity")
           print(likes_entity)

           if likes_entity.pk > 0:
            result["success"] = True
            result["result"] = Likes.objects.filter(ideaID=like_dto["ideaID"]).first()
            result["error"] = []
            return result
           return result

    except Exception as error:
           print("add_like error")
           print(error)
           result["success"] = False
           result["result"] = like_dto
           result["error"].append(error)
    return result