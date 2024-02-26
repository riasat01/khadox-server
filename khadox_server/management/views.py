# from django.shortcuts import render
from .serializers import DistrictSerializer, RestaurantSerializer, FoodSerializer
from .models import District, Restaurant, Food
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view

# Create your views here.
@api_view(['GET', 'POST'])
def district_list(request, format=None):
    if request.method == 'GET':
        print('PRINTING REQUEST', request)
        print('REQUEST PRINTED')
        district = District.objects.all()
        serializer = DistrictSerializer(district, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = DistrictSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
def restaurant_list(request, format=None):

    if request.method == 'GET':
        restaurant = Restaurant.objects.all()
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = RestaurantSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET'])
def restaurant_by_district(request, name, format=None):

    if request.method == 'GET':
        restaurant = Restaurant.objects.filter(district=name)
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data)
    
@api_view(['GET', 'POST'])
def restaurant_by_id(request, id, format=None):

    if request.method == 'GET':
        restaurant = Restaurant.objects.filter(pk=id)
        serializer = RestaurantSerializer(restaurant, many=True)
        return Response(serializer.data)


@api_view(['GET', 'POST'])
def food_list(request, format=None):

    if request.method == 'GET':
        food = Food.objects.all()
        serializer = FoodSerializer(food, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        # data = JSONParser().parse(request)
        serializer = FoodSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)