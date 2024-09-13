import json
import django
from django.conf import settings
from .models import Users
from .models import Ideas
from .models import Comments
from datetime import datetime

def add_comment(comment_dto): 
    
    result = {"success": False, "result": None, "error": []}
    
    try:     
           print(comment_dto) 
           date = datetime.now();

           user = Users.objects.filter(id=comment_dto["userID"]).first()
           print("#add_comment user")
           print(user)

           if user is None:
            result["success"] = False
            result["result"] = comment_dto
            result["error"].append("user doesn't exist for " .format(comment_dto["userID"]))
            return result

           idea = Ideas.objects.filter(id=comment_dto["ideaID"]).first()
           print("#add_comment idea")
           print(idea)

           if idea is None:
            result["success"] = False
            result["result"] = comment_dto
            result["error"].append("Idea doesn't exist for {0}" .format(comment_dto["ideaID"]))
            return result

           comments_entity = Comments(userID = user, ideaID = idea, Comment = comment_dto["comment"], comment_date = date)
           
           comments_entity.save()

           print("#add_comment comments_entity")
           print(comments_entity)

           if comments_entity.pk > 0:
            result["success"] = True
            result["result"] = Comments.objects.filter(ideaID=comment_dto["ideaID"]).first()
            result["error"] = []
            return result
           return result

    except Exception as error:
           print("add_comment error")
           print(error)
           result["success"] = False
           result["result"] = comment_dto
           result["error"].append(error)
    return result