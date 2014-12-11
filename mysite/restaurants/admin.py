from django.contrib import admin
from restaurants.models import Restaurant, Food


class RestaurantAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone_number', 'address')
    search_fields = ('name',)


class FoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'restaurant', 'price')
    list_filter = ('is_spicy',)
    ordering = ('-price',)


admin.site.register(Restaurant, RestaurantAdmin)
admin.site.register(Food, FoodAdmin)
