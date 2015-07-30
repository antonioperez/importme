from django.contrib.auth.models import User
from rest_framework import serializers
from blog.models import *

class UserSerializer(serializers.ModelSerializer):
    #commenter = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'email', "first_name", "last_name")

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ('id','post', 'content', 'parent', 'children_comment', 'upvotes', 'downvotes', 'parent')

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = ('tag','id')

class PostSerializer(serializers.ModelSerializer):
    post_comments = CommentSerializer(many=True, read_only=True)
    class Meta:
        model = Post
        fields = ('id','user','subject','content', 'post_comments', 'tags', 'created', 'modified')
        depth = 1