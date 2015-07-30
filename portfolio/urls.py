from django.conf.urls import include, url
from portfolio.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'projects', ProjectViewSet)

urlpatterns = [
    url(r'^', include(router.urls)),
]
