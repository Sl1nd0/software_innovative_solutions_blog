import traceback
import json
from .models import Users
from .models import Topics
from .models import Ideas
from .models import Likes
from .models import Comments
from .models import IdeasTopics
from datetime import datetime

def list_comments_by_idea_query(idea): 

	result = {"success": False, "result": {}, "error": []}
	print("idea")
	print(idea)

	try: 
		comments_result = Comments.objects.filter(ideaID=idea["ideaID"]).values()
		print(comments_result)

		comments = []

		comment_dto = {'id': 0, 
			'ideaID_id': 0,
			'canEdit': 0,
			'userID_id': 0, 
			'Comment': "",
			'comment_date': datetime.now()
			}

		for comment in comments_result:
		 if comment['userID_id'] == int(idea["userID"]):
			 comment_dto['id'] = comment["id"]
			 comment_dto['ideaID_id'] = comment["ideaID_id"];
			 comment_dto['canEdit'] = 1;
			 comment_dto['userID_id'] = comment["userID_id"];
			 comment_dto['Comment'] = comment["Comment"];
			 comment_dto['comment_date'] = comment["comment_date"];
			 comments.append(comment_dto)
			 continue		 
		 comment_dto['id'] = comment["id"];
		 comment_dto['ideaID_id'] = comment["ideaID_id"];
		 comment_dto['canEdit'] = 0;
		 comment_dto['userID_id'] = comment["userID_id"];
		 comment_dto['Comment'] = comment["Comment"];
		 comment_dto['comment_date'] = comment["comment_date"];
		 print("comment_dto ")
		 print(comment_dto)
		 comments.append(comment_dto)

		if comments_result is None:
			result["error"].append("No comments retrieved for idea {0}" .format(idea))
			return result
		else:
			result["success"] = True
			result["result"] = comments
			result["error"] = None
			return result

		return result

	except Exception as error:
			print("list_comments_by_idea_query error")
			print(error)
			result["success"] = False
			result["result"] = idea
			result["error"].append(error)	
	return result