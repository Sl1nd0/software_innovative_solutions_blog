from . import user_roles_queries
from .models import Users

def get_user_name_and_sur(userid):
  print(userid)
  user_result = Users.objects.filter(id=userid).first()
  details = user_result.name + " " + user_result.surname
  print("details")
  print(details)
  print("details")
  return details