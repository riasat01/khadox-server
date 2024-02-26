from django.contrib import admin
from .models import District, Restaurant, Food

# Register your models here.
admin.site.register(District)
admin.site.register(Restaurant)
admin.site.register(Food)