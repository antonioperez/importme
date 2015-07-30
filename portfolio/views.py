from rest_framework import viewsets
from rest_framework.response import Response

from portfolio.serializers import *
from portfolio.models import *

class ProjectViewSet(viewsets.ModelViewSet):
	queryset = Project.objects.all()
	serializer_class = ProjectSerializer