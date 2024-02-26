from rest_framework import serializers
from .models import District, Restaurant, Food

class DistrictSerializer(serializers.ModelSerializer):
    class Meta:
        model = District
        fields = ['id', 'name', 'image_url']

class RestaurantSerializer(serializers.ModelSerializer):
    class Meta:
        model = Restaurant
        fields = ['id', 'restaurant_name', 'restaurant_address', 'cover_photo', 'district', 'ratings', 'number_of_raters']

   
class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'food_name', 'food_image', 'price', 'ratings', 'number_of_raters', 'restaurant']
