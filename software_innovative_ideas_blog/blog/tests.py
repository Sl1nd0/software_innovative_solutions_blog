import django
from django.conf import settings
from django.db import connections, transaction
from .models import UserRoles
from . import users_roles_handlers_tests
from . import users_handlers_tests
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
    users_roles_handlers_tests.add_user_role_success_test({"role": "test"}) 
    users_roles_handlers_tests.add_user_role_fail_test({})
    
    #users_handlers_tests unit tests
    users_handlers_tests.add_user_success_test({})
    users_handlers_tests.add_user_fail_test({})

set_up_test_db()