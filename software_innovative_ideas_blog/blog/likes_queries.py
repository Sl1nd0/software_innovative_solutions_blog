import traceback
import json
from .models import Users
from .models import Topics
from .models import Ideas
from .models import Likes
from .models import Comments
from .models import IdeasTopics
from datetime import datetime

def list_likes_by_idea_query(idea):
	result = {"success": False, "result": {}, "error": []}
	print("idea")
	print(idea)

	try: 
		likes_result = Likes.objects.filter(ideaID=idea).values()
		print(likes_result )

		if likes_result is None:
			result["error"].append("No likes retrieved for idea {0}" .format(idea))
			return result
		else:
			result["success"] = True
			result["result"] = likes_result
			result["error"] = None
			return result

		return result

	except Exception as error:
			print("list_likes_by_idea_query error")
			print(error)
			result["success"] = False
			result["result"] = idea
			result["error"].append(error)	
	return result