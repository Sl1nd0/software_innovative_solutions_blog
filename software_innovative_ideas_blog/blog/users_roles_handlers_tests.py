import sqlite3
import sys
from . import user_roles_handlers

def add_user_role_success_test(role):
     result = user_roles_handlers.add_user_role(role)     
     if (result["result"] != None):
        print("user_roles_handlers_tests: role added successfully")

def add_user_role_fail_test(role):
     result = user_roles_handlers.add_user_role(role)
     if (result["error"] != None):
       print("user_roles_handlers_tests: failed adding a role, reason {0}" .format(result["error"][0]))
