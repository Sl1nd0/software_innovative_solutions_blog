from django.db import models
from datetime import datetime

# Create your models here.
# Register your models here.
class Users(models.Model):
	user_name = models.CharField(max_length=255)
	name = models.CharField(max_length=255, default= '')
	birthdate = models.CharField(max_length=255)
	surname = models.CharField(max_length=255, default= '')
	email = models.CharField(max_length=255, default= '')
	identifier = models.CharField(max_length=255, default= '')
	password = models.CharField(max_length=255)
	cell_number = models.CharField(max_length=80)
	user_date = models.DateTimeField(max_length=50)