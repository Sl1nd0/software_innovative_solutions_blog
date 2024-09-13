from . import user_roles_queries

def get_user_role(userid):
  role_result = user_roles_queries.get_user_role_by_user_id_query(userid)
  print("role_result")
  role = role_result["result"].role
  print("role_result")
  return role