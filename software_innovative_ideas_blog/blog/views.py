from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Users
from .forms import NameForm
import sys
from . import users_handlers
from . import topics_handlers
from . import users_queries
from . import topics_queries
from datetime import datetime

def landing(request):
  listtopicsqueryresult = topics_queries.list_topics_query();
  template = loader.get_template('landing.html')

  if listtopicsqueryresult["success"] == True:
    context = {"topics": listtopicsqueryresult["result"]}
    return HttpResponse(template.render(context, request))

  context = { }
  return HttpResponse(template.render(context, request))
  
def main(request):
  template = loader.get_template('index.html')
  context = { }
  return HttpResponse(template.render(context, request))

def logout(request):
  #users = Users.objects.all().values()
  return HttpResponseRedirect("/login/") 

def login(request):

    if request.method == "POST":
        user = {
            "email": request.POST.get("email"),
            "user_name": request.POST.get("email"),
            "password": request.POST.get("password"),
        }

        user_login_queryresult = users_queries.user_login_query(user)

        if user_login_queryresult["success"] == True:
         return HttpResponseRedirect("/landing/")
        else:
         template = loader.get_template('login.html')
         context = {"error":user_login_queryresult["Error"][0]} 
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
            "identifier": request.POST.get("identifier"),
            "password": request.POST.get("password"),
            "cell_number": request.POST.get("number"),
            "birthdate": request.POST.get("birthdate")
        }
        
        adduserresult = users_handler.add_user(user)

        if adduserresult["success"] == True:
         return HttpResponseRedirect("/login/")
        else:
            template = loader.get_template('createaccount.html')
            context = {"error":adduserresult["Error"][0]} 
        return HttpResponse(template.render(context, request))

    template = loader.get_template('createaccount.html')
    context = {}
    return HttpResponse(template.render(context, request))

def topics(request):
    
    listtopicsqueryresult = topics_queries.list_topics_query();

    if listtopicsqueryresult["success"] == True:
        template = loader.get_template('topics.html')
        context = {"topics": listtopicsqueryresult["result"]}
        return HttpResponse(template.render(context, request))

    template = loader.get_template('topics.html')
    context = {}
    return HttpResponse(template.render(context, request))
    
def edittopic(request, id):
    #Add edit handler
    topic = topics_queries.get_topic_by_id_query(id)

    template = loader.get_template('edittopic.html')
    context = {"topic": topic["result"]["topic"]}
    return HttpResponse(template.render(context, request))
    
def deletetopic(request, id):
    #Add delete handler
    topic = topics_queries.get_topic_by_id_query(id)

    template = loader.get_template('deletetopic.html')
    context = {"topic": topic["result"]["topic"]}
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
            context = {"error":addtopicresult["Error"][0]} 
        return HttpResponse(template.render(context, request))

    template = loader.get_template('addtopic.html')
    context = {}
    return HttpResponse(template.render(context, request))