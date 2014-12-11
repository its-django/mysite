from django.contrib import admin
from restaurants.models import Restaurant, Food


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
