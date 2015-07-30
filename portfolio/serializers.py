from django.contrib.auth.models import User
from rest_framework import serializers
from portfolio.models import *

class ProjectSerializer(serializers.ModelSerializer):
	class Meta:
		model = Project
		fields = ('user','title', 'description', 'code', 'website', 'image')
