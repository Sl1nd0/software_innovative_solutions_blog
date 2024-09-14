import django
from django.conf import settings
from django.db import connections, transaction
from .models import UserRoles
from . import topics_handlers
from . import users_roles_handlers_tests
from . import ideas_handlers_tests
from . import users_handlers_tests
from . import ideas_queries_tests
from django.conf import settings
from django.test import TestCase
from django.core.management import call_command

def set_up_test_db():
    
    try:
        new_db_settings = {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': ':memory:',
        }

        settings.DATABASES['default'].update(new_db_settings)
        print('In memory database setup complete')

        # Apply all migrations
        call_command('migrate', 'blog', interactive=False)              

    except Exception as e:
        print(f"Error running migrations: {e}")

    #user_roles_handlers_tests unit tests    
    users_roles_handlers_tests.add_user_role_success_test({"role": "administrator"})
    users_roles_handlers_tests.add_user_role_success_test({"role": "user"})
    users_roles_handlers_tests.add_user_role_fail_test({})     
    
    #users_handlers_tests unit tests
    users_handlers_tests.add_user_success_test({
        "name": "test",
        "surname": "test",
        "email": "test@gmail.com",
        "user_name": "test@gmail.com",
        "identifier": "testIdPass",
        "password": "testPass123",
        "cell_number": "testPass123",
        "birthdate": "1999/01/12"
    })
    users_handlers_tests.add_user_fail_test({})

    topics_handlers.add_topic({"topic":"test"})
     #ideas_handlers_tests unit tests    
    ideas_handlers_tests.add_idea_success_test({'topicID': 1, 'idea': 'fghgh', 'userID': 1})
    ideas_handlers_tests.add_idea_fail_test({}) 

    #ideas_queries_tests get_ideas_and_topics_query_success_test
    ideas_queries_tests.get_ideas_and_topics_query_success_test({"userID": 1})

set_up_test_db()