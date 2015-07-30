from django.db import models
from django.contrib.auth.models import User


class Project(models.Model):
	user = models.ForeignKey(User, related_name='projects')
	title = models.CharField(max_length=100)
	description = models.TextField(blank = True)
	code = models.CharField(max_length = 100)
	website = models.CharField(max_length = 100)
	image = models.CharField(max_length = 200)
	date_start = models.DateTimeField(null=True)
	date_end = models.DateTimeField(null=True)
	modified = models.DateTimeField(auto_now=True)
	created = models.DateTimeField(auto_now_add=True)
