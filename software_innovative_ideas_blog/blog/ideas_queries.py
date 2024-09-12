import traceback
import json
from .models import Users
from .models import Topics
from .models import Ideas
from .models import Likes
from .models import Comments
from .models import IdeasTopics
from datetime import datetime

def user_login_query(user): 

	result = {"success": False, "result": {}, "error": []}

	try:            
		email = user['email']
		password = user['password']
		user_login_result = Users.objects.filter(username=email, password=password).values()
	
		if user_login_result is None:
			return result
		else:
			result["success"] = True
			result["result"] = user_login_result
			result["error"] = None
			return result

		return result

	except Exception as error:
			result["success"] = False
			result["result"] = user
			result["error"].append(error)	
	return result

def get_ideas_and_topics_query(user):
	print("#get_ideas_and_topics_query")
	print(user)
	#1st one should be my idea

	result = {"success": False, "result": {}, "error": []}
	ideas = []

	try:
		print("user")
		print(user)

		idea_query_result = Ideas.objects.filter().values()
		my_user_details = Users.objects.filter(id = user["userID"]).values().first()
		print(my_user_details)

		other_user_details = Users.objects.all().values()
		print(other_user_details)

		my_idea = idea_query_result.filter(userID = user["userID"]).first()
		print("idea_query_result")
		print(my_idea)

		idea_topic_query_result = IdeasTopics.objects.all().values()
		print("idea_topic_query_result")
		print(idea_topic_query_result)

		if idea_topic_query_result is None:
			return result

		print(idea_topic_query_result[0])
		my_topic = None

		if my_idea != None:
		  my_topic = idea_topic_query_result.filter(ideaID = my_idea["id"]).first()
		  my_likes = Likes.objects.filter(ideaID = my_idea["id"]).count()
		  my_comments = Comments.objects.filter(ideaID = my_idea["id"]).count();
		  
		if my_topic != None:
			ideas.append({
				"name": my_user_details["name"],
				"surname": my_user_details["surname"],
				"userID": my_user_details["id"],
				"idea": my_idea["idea"],
				"ideaID": my_idea["id"],
				"topic": Topics.objects.filter(id=my_topic['topicID_id']).values().first()["topic"],
				"likes": my_likes,
				"comments": my_comments
			})

		for idea in idea_query_result:			
			current_topic = idea_topic_query_result.filter(ideaID = idea["id"]).first()
			likes = Likes.objects.filter(ideaID = idea["id"]).count();
			comments = Comments.objects.filter(ideaID = idea["id"]).count();

			print("comments")
			print(idea["id"])
			print(current_topic)

			if current_topic != None:
				ideas.append({
				"name":other_user_details.filter(id=idea["userID_id"]).first()["name"],
				"surname": other_user_details.filter(id=idea["userID_id"]).first()["surname"],
				"userID": idea["userID_id"],
				"idea": idea["idea"],
				"ideaID": idea["id"],
				"topic": Topics.objects.filter(id=current_topic['topicID_id']).values().first()["topic"],
				"likes": likes,
				"comments": comments
				})
		
		distinct_ideas = list(map(dict, set(frozenset(d.items()) for d in ideas)))

		if len(distinct_ideas) > 0:
			result["success"] = True
			result["result"] = distinct_ideas
			return result
		return result

	except Exception as error:
			print("get_ideas_and_topics_query error")
			print(error)
			stack_trace = traceback.format_exc()
			print(stack_trace)
			result["success"] = False
			result["result"] = user
			result["error"].append(error)	
	return result