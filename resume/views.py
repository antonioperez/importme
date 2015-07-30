from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response

from resume.serializers import *
from resume.models import *


class ResumeViewSet(viewsets.ModelViewSet):
    queryset = Resume.objects.all()
    serializer_class = ResumeSerializer

class RowViewSet(viewsets.ModelViewSet):
    queryset = Row.objects.all()
    serializer_class = RowSerializer