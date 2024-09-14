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
			'CommentID': 0,
			'comment_date': datetime.now()
			}

		#idea["userID
		print("idea[userID]")
		print(idea["userID"])
		for comment in comments_result:
		 canedit = 0;
		 if comment['userID_id'] == idea["userID"]:
		  canedit = 1;

		 comments.append({'id': comment["id"], 
			'ideaID_id': comment["ideaID_id"],
			'canEdit': canedit,
			'userID_id': comment["userID_id"], 
			'Comment': comment["Comment"],
			'commentID': comment["id"],
			'comment_date': comment["comment_date"]
			})

		 print("comment_dto ")
		 print(comments)
		 comments.append(comment_dto)

		comments.sort(key=lambda x: x["id"]) 

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