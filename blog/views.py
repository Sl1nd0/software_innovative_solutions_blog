from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.template import loader
from .models import Users
from .forms import NameForm
import sys
from . import users_handler
from . import users_queries
from datetime import datetime

# Create your views here.
def users(request):
  #users = Users.objects.all().values()
  template = loader.get_template('createaccount.html')
  context = { }
  return HttpResponse(template.render(context, request))
  
def landing(request):
  #users = Users.objects.all().values()
  template = loader.get_template('landing.html')
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
         return HttpResponseRedirect("/createaccount/") 

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
         return HttpResponseRedirect("/createaccount/") 

    template = loader.get_template('createaccount.html')
    context = { }
    return HttpResponse(template.render(context, request))