from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Users
import sys
from . import users_handlers
from . import topics_handlers
from . import users_queries
from . import user_roles_queries
from . import topics_queries
from . import ideas_queries
from . import ideas_handlers
from . import likes_handlers
from . import comments_handlers
from . import user_roles_seed
from . import comments_queries
from datetime import datetime

def landing(request):
  context = {"topics":"", "userid": "", "role": "", "error": "", "ideas": []}
  template = loader.get_template('landing.html')
  
  listtopicsqueryresult = topics_queries.list_topics_query();

  if listtopicsqueryresult["success"] == True:
    context["topics"] = listtopicsqueryresult["result"]

  if request.method == "POST":
    
    user = {
    "email": request.POST.get("user_name"),
    "user_name": request.POST.get("user_name"),
    "password": request.POST.get("password"),
    }

    user_login_queryresult = users_queries.user_login_query(user)
    
    if user_login_queryresult["success"] == False:
        context["error"] = user_login_queryresult["error"][0]
        template = loader.get_template('login.html')
        return HttpResponse(template.render(context, request))
    
    ideas_queries_result = ideas_queries.get_ideas_and_topics_query({"userID": user_login_queryresult["result"]["id"]})

    print(ideas_queries_result["result"])
    role_query_result = user_roles_queries.get_user_role_by_id_query(user_login_queryresult["result"]["User_roleID_id"])
    print(role_query_result)    
    context["userid"] = user_login_queryresult["result"]["id"]
    context["role"] = role_query_result["result"]["role"]
    context["ideas"] = ideas_queries_result["result"]
    return HttpResponse(template.render(context, request))
  
  return HttpResponse(template.render(context, request))
  
#main_landing
def main_landing(request, id):
  
  context = {"topics":"", "userid": "", "ideas": []}
  template = loader.get_template('landing.html')

  listtopicsqueryresult = topics_queries.list_topics_query();

  if listtopicsqueryresult["success"] == True:
    context["topics"] = listtopicsqueryresult["result"]

    user = {
    "id": id
    }

    get_user_by_id_queryresult = users_queries.get_user_by_id_query(user)
    ideas_queries_result = ideas_queries.get_ideas_and_topics_query({"userID": get_user_by_id_queryresult["result"]["id"]})
    print(ideas_queries_result["result"])
    print(get_user_by_id_queryresult)
    context["userid"] = get_user_by_id_queryresult["result"]["id"]
    context["ideas"] = ideas_queries_result["result"]
    return HttpResponse(template.render(context, request))
  
  return HttpResponse(template.render(context, request))

def main(request):
  template = loader.get_template('index.html')
  context = { }

  #user roles seed
  seedresult = user_roles_seed.user_roles_seed()

  if seedresult["success"] == False:
    context = {"error": seedresult["error"][0]} 
    return HttpResponse(template.render(context, request))
  
  context = {}
  return HttpResponse(template.render(context, request))

def logout(request):
  #users = Users.objects.all().values()
  return HttpResponseRedirect("/login/") 

def login(request):

    if request.method == "POST":

        user = {
            "email": request.POST.get("email"),
            "user_name": request.POST.get("email"),
            "password": request.POST.get("password")
        }

        user_login_queryresult = users_queries.user_login_query(user)

        if user_login_queryresult["success"] == True:
         return HttpResponseRedirect("/landing/")
        else:
         template = loader.get_template('login.html')
         context = {"error":user_login_queryresult["error"][0]}
         return HttpResponse(template.render(context, request))

    template = loader.get_template('login.html')
    context = { }
    return HttpResponse(template.render(context, request))

def createaccount(request):

    if request.method == "POST":
       
        user = {
            "name": request.POST.get("name"),
            "surname": request.POST.get("surname"),
            "email": request.POST.get("email"),
            "user_name": request.POST.get("email"),
            "email": request.POST.get("email"),
            "identifier": request.POST.get("identifier"),
            "password": request.POST.get("password"),
            "cell_number": request.POST.get("number"),
            "birthdate": request.POST.get("birthdate")
        }
        
        adduserresult = users_handlers.add_user(user)

        if adduserresult["success"] == True:
         return HttpResponseRedirect("/login/")
        else:
            template = loader.get_template('createaccount.html')
            context = {"error":adduserresult["error"][0]} 
            return HttpResponse(template.render(context, request))

    template = loader.get_template('createaccount.html')
    context = {}
    return HttpResponse(template.render(context, request))

def topics(request, userid):
    print(userid)
    listtopicsqueryresult = topics_queries.list_topics_query();

    if listtopicsqueryresult["success"] == True:
        template = loader.get_template('topics.html')
        context = {"topics": listtopicsqueryresult["result"], "userid": userid}
        return HttpResponse(template.render(context, request))

    template = loader.get_template('topics.html')
    context = {"userid": userid}
    return HttpResponse(template.render(context, request))
    
def edittopic(request, id):
    
    topic = topics_queries.get_topic_by_id_query(id)

    if request.method == "POST":
       
        topic_dto = {
            "topic": request.POST.get("topic"),
            "id": id
        }
        
        edittopicresult = topics_handlers.edit_topic(topic_dto)
        
        if edittopicresult["success"] == True:
         return HttpResponseRedirect("/topics/")
        else:
            template = loader.get_template('edittopic.html')
            print(topic)
            context = {"error":edittopicresult["error"][0], "topic": topic["result"]} 
            return HttpResponse(template.render(context, request))
    
    template = loader.get_template('edittopic.html')
    context = {"topic": topic["result"]}
    return HttpResponse(template.render(context, request))
    
def deletetopic(request, id):

    if request.method == "POST":
        
        edittopicresult = topics_handlers.delete_topic(id)
        
        if edittopicresult["success"] == True:
         return HttpResponseRedirect("/topics/")
        else:
            template = loader.get_template('deletetopic.html')
            print(topic)
            context = {"error":edittopicresult["error"][0], "topic": topic["result"]} 
            return HttpResponse(template.render(context, request))

    topic = topics_queries.get_topic_by_id_query(id)
    template = loader.get_template('deletetopic.html')
    context = {"topic": topic["result"]}
    return HttpResponse(template.render(context, request))

def addtopic(request):

    if request.method == "POST":
       
        topic = {
            "topic": request.POST.get("topic")
        }
        
        addtopicresult = topics_handlers.add_topic(topic)
        
        print(addtopicresult)

        if addtopicresult["success"] == True:
         return HttpResponseRedirect("/topics/")
        else:
            template = loader.get_template('addtopic.html')
            context = {"error":addtopicresult["error"][0]} 
            return HttpResponse(template.render(context, request))

    template = loader.get_template('addtopic.html')
    context = {}
    return HttpResponse(template.render(context, request))

###POSTS ideas
def addidea(request, userid):
    context = {"topics":[], "userid": "", "role": "", "error": ""}
    context["userid"] = userid;

    template = loader.get_template('addidea.html')

    if request.method == "POST":

        idea = {
            "topicID": request.POST.get("topic"),
            "idea": request.POST.get("idea"),
            "userID": userid
        }
        
        addidearesult= ideas_handlers.add_idea(idea)
        
        print(addidearesult)
                
        return HttpResponse(template.render(context, request))

    listtopicsqueryresult = topics_queries.list_topics_query();

    if listtopicsqueryresult["success"] == True: 
     context["topics"] = listtopicsqueryresult["result"]
    
    return HttpResponse(template.render(context, request))

#comments
def addcomment(request, userid):
    context = {"topics":[], "userid": "", "role": "", "error": "", "ideadata": "", "comments": ""}
    context["userid"] = userid;
     
    template = loader.get_template('addcomment.html')

    if request.method == "POST":

        comment_dto = {
            "idea": request.POST.get("idea"),
            "ideaID": request.POST.get("ideaID"),
            "userID": userid
        }
        
        list_comments_queries = comments_queries.list_comments_by_idea_query(comment_dto["ideaID"])

        all_comments = []

        for comment in list_comments_queries["result"]:
            all_comments.append({
                "comment": comment["Comment"],
                "date": comment["comment_date"],
                "name": "Test",
                "surname": "Test"
            })

        print("list_comments_queries[result]")
        print(list_comments_queries["result"])
        context["comments"] = all_comments

        print("comment_dto")
        print(comment_dto)

        context["idea"] = comment_dto["idea"];
        context["ideaID"] = comment_dto["ideaID"];
        context["userid"] = userid;
        return HttpResponse(template.render(context, request))

    return HttpResponse(template.render(context, request))

def comment(request, userid):
    context = {"topics":[], "userid": "", "role": "", "error": "", "ideadata": ""}
    context["userid"] = userid;

    template = loader.get_template('addcomment.html')

    if request.method == "POST":
            
        comment_dto = {
            "idea": request.POST.get("idea"),
            "ideaID": request.POST.get("ideaID"),
            "userID": userid,
            "comment":request.POST.get("form_comment")
        }
         
        list_comments_queries = comments_queries.list_comments_by_idea_query(comment_dto["ideaID"])

        all_comments = []

        for comment in list_comments_queries["result"]:
            all_comments.append({
                "comment": comment["Comment"],
                "date": comment["comment_date"],
                "name": "Test",
                "surname": "Test"
            })

        print("list_comments_queries[result]")
        print(list_comments_queries["result"])
        context["comments"] = all_comments

        print("comment_dto")
        print(comment_dto)

        add_comment_result = comments_handlers.add_comment(comment_dto)
        print(add_comment_result["result"])

        context["idea"] = comment_dto["idea"];
        context["ideaID"] = comment_dto["ideaID"];
        context["userid"] = userid;
        return HttpResponseRedirect("/addcomment/"+str(userid))

    return HttpResponseRedirect("/addcomment/"+str(userid))

#likes
def addlike(request, userid):
    context = {"topics":[], "userid": "", "role": "", "error": ""}
    context["userid"] = userid;

    template = loader.get_template('addlike.html')

    if request.method == "POST":
        like_dto = {
            "idea": request.POST.get("idea"),
            "ideaID": request.POST.get("ideaID"),
            "userID": userid
        }
        print("like_dto")
        print(like_dto)
        like_result = likes_handlers.add_like(like_dto)
        print("like_result")
        print(like_result["error"])
        print(like_result["result"])
        return HttpResponseRedirect("/landing/"+str(userid))
                    
    return HttpResponseRedirect("/landing/"+str(userid))