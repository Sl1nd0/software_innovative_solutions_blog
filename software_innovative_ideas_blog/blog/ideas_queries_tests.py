import sqlite3
import sys
from . import ideas_queries

def get_ideas_and_topics_query_success_test(user):
     result = ideas_queries.get_ideas_and_topics_query(user)     
     if (result["result"] != None):
        print("get_ideas_and_topics_query_success_test: ideas {0} retrieved successfully" .format(result["result"]))

def get_ideas_and_topics_query_fail_test(user):
     result = ideas_queries.get_ideas_and_topics_query(user)     
     if (result["error"] != None):
       print("get_ideas_and_topics_query_fail_test: failed getting an idea, reason {0}" .format(result["error"][0]))
