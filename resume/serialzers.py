from django.contrib.auth.models import user
from rest_framework import serializers
from resume.models import *

class ResumeSerializer(serializers.ModelSerializer):
	class Meta:
		model = Resume
		fields ('id', 'user' ,'isActive', 'created', 'modified')

class RowSerializer(serializers.ModelSerializer):
	class Meta:
		model = Row
		fields ('id', 'heading' ,'start_date', 'end_date')

class RowDetailsSerializer(serializers.ModelSerializer):
	class Meta:
		model = Row
		fields ('id', 'heading' ,'content', 'row')
		depth = 1