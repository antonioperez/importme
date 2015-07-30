from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.response import Response

from blog.serializers import *
from blog.models import *

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def retrieve(self, request, pk):
        try:
            user = User.objects.get(pk=pk)
        except User.DoesNotExist:
            user = {}
        user.password = ''
        resp = UserSerializer(user)
        return Response(resp.data)

    def create(self, request):
        data = request.data
        email = data.get('email')
        username = data.get('username')
        password = data.get('password')
        first_name = data.get('first_name')
        last_name = data.get('last_name')
        user = User.objects.create_user(email=email, username=username, password=password,
                                        first_name=first_name, last_name=last_name)
        data.password = user.password
        return Response(data)
        
class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created')
    serializer_class = PostSerializer

    def get_tag(self, pk):
        try:
            tag = Tag.objects.get(pk = pk)
        except:
            tag = {}
        return tag

    def create(self, request):
        data = request.data
        tags = data.get('tags')
        subject = data.get('subject')
        content = data.get('content')
        post_tags = []
        post = Post(user = request.user, subject = subject, content = content)
        post.save()

        for tag_pk in tags:
            tag = self.get_tag(tag_pk)
            post.tags.add(tag)
            post_tags.append(tag.tag)

        data['tags'] = post_tags;
        return Response(data)


class TagViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer





