from django.db import models
from django.contrib.auth.models import User


class Resume(models.Model):
	user = models.ForeignKey(User, related_name='resumes')
	isActive = models.BooleanField(default = False)
	created = models.DateTimeField(auto_now_add = True)
	modified = models.DateTimeField(auto_now = True)

class Layout(models.Model):
	css_code = models.TextField(blank = True)
	resume = models.ForeignKey(Resume, related_name='resume_styles')

class Row(models.Model):
	heading = models.CharField(max_length = 100)
	start_date = models.DateTimeField()
	end_date = models.DateTimeField()

class RowDetails(models.Model):
	row = models.ForeignKey(Row, related_name='row_details')
	heading = models.CharField(max_length = 100)
	content = models.TextField(null=True)
