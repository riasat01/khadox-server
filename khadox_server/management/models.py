from django.db import models

# Create your models here.
class District(models.Model):
    name = models.CharField(max_length=50, unique=True, null=False, blank=False)
    image_url = models.URLField(max_length=255, null=False, blank=False)

    def __str__(self):
        return f"{self.name} - {self.image_url}"


class Restaurant(models.Model):
    restaurant_name = models.CharField(max_length=255, null=False, blank=False)
    restaurant_address = models.CharField(max_length=255, null=False, blank=False)
    cover_photo = models.URLField(max_length=255, null=False, blank=False)
    district = models.ForeignKey(District, on_delete=models.CASCADE, null=False, blank=False)
    ratings = models.FloatField(default=0.0, null=False, blank=False)
    number_of_raters = models.PositiveIntegerField(default=0, null=False, blank=False)

    def __str__(self):
        return f"{self.restaurant_name}, {self.restaurant_address}, {self.cover_photo}, {self.district.name}, {self.ratings}, {self.number_of_raters}"


class Food(models.Model):
    food_name = models.CharField(max_length=50, null=False, blank=False)
    food_image = models.URLField(max_length=255, null=False, blank=False)
    price = models.DecimalField(max_digits=7, decimal_places=2, null=False, blank=False)
    ratings = models.FloatField(default=0.0, null=False, blank=False)
    number_of_raters = models.PositiveIntegerField(default=0, null=False, blank=False)
    restaurant = models.ForeignKey(Restaurant, on_delete=models.CASCADE, null=False, blank=False)

    def __str__(self):
        return f"{self.food_name}, {self.food_image}, {self.price}, {self.ratings}, {self.number_of_raters}, {self.restaurant.restaurant_name}"


