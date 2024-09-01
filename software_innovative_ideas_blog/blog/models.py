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

class Ideas(models.Model):
	userID = models.ForeignKey(Users, on_delete=models.CASCADE)
	idea = models.TextField(default= '') 
	idea_date = models.DateTimeField(max_length=50)

class Topics(models.Model):
	topic = models.CharField(max_length=255)
	topic_date = models.DateTimeField(max_length=50)

class IdeasTopics(models.Model):
	ideaID = models.ForeignKey(Ideas, on_delete=models.CASCADE)
	topicID = models.ForeignKey(Topics, on_delete=models.CASCADE)

class Likes(models.Model):
	ideaID = models.ForeignKey(Ideas, on_delete=models.CASCADE)
	userID = models.ForeignKey(Users, on_delete=models.CASCADE)
	like_date = models.DateTimeField(max_length=50)

class Comments(models.Model):
	ideaID = models.ForeignKey(Ideas, on_delete=models.CASCADE)
	userID = models.ForeignKey(Users, on_delete=models.CASCADE)
	Comment = models.TextField(default= '')
	comment_date = models.DateTimeField(max_length=50)