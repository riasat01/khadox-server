from django.urls import path
from . import views

###########################
from rest_framework.urlpatterns import format_suffix_patterns
###########################

app_name = "management"
urlpatterns = [
    ############
    path("api/district/", views.district_list, name="district"),
    path("api/restaurant/", views.restaurant_list, name="restaurant_api"),
    path("api/restaurant/<slug:name>/", views.restaurant_by_district, name="restaurant_by_district"),
    path("api/restaurant/specific/<int:id>/", views.restaurant_by_id, name="restaurant_by_id"),
    path("api/food/", views.food_list, name="food_api"),
    ############
]

######################
urlpatterns = format_suffix_patterns(urlpatterns)
######################