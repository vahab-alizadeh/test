from http.client import HTTPResponse

from django.shortcuts import render

from todo import models
from todo.models import Todo
from django.http import JsonResponse
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
def index(request):
    context = {
        'todos':Todo.objects.all()
    }
    return render(request,'home/index.html',context)

@api_view(['GET'])
def todos_json(request):
    todos=list(Todo.objects.all().values('title','is_done'))
    return Response({'todos':todos},status.HTTP_200_OK)