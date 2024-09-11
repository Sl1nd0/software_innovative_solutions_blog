import json
from .models import Users
from datetime import datetime
from . import users_handlers

def add_user_success_test(user): 
    result = users_handlers.add_user(user)
    if result["result"] != None:
        print("add_user_success_test: user {0} added successfully" .format(result["result"]))

def add_user_fail_test(user): 
    result = users_handlers.add_user(user)
    if result["error"] != None:
        print("add_user_fail_test: failed adding a user, reason {0}" .format(result["error"][0]))