from django.conf.urls import include, url
from blog.views import *


urlpatterns = [
    url(r'^', BlogFront),


]
