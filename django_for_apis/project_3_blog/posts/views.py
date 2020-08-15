from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import permissions
from posts.models import Post
from posts.serializers import PostSerializer
from posts.permissions import IsAuthorOrReadOnly


class PostList(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer


class PostDetail(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthorOrReadOnly,)
    queryset = Post.objects.all()
    serializer_class = PostSerializer
