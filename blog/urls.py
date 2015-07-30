from django.conf.urls import include, url
from blog.views import *

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)
router.register(r'tags', TagViewSet) 
router.register(r'users', UserViewSet, 'users')

urlpatterns = [
    url(r'^', include(router.urls)),
]
