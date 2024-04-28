from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(["GET", "POST"])
def user (request, format=None):
    if request.method == "POST":
        print(request.data)
        return Response(request.data, status=status.HTTP_201_CREATED)