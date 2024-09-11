import json
from .models import Users
from datetime import datetime
from . import ideas_handlers

def add_idea_success_test(idea): 
    result = ideas_handlers.add_idea(idea)
    if result["result"] != None:
        print("add_idea_success_test: idea {0} added successfully" .format(result["result"]))

def add_idea_fail_test(idea): 
    result = ideas_handlers.add_idea(idea)
    if result["error"] != None:
        print("add_idea_fail_test: failed adding an idea, reason {0}" .format(result["error"][0]))