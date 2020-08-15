from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from rest_framework import serializers
from todos.serializers import TodoSerializer
from todos.models import Todo


class ListTodo(generics.ListAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer


class DetailsTodo(generics.RetrieveAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer
