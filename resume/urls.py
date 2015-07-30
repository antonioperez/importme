from django.conf.urls import include, url
from resume.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'resumes', ResumeViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
