from django.contrib import admin
from . models import CarBrand, CarModel, UserCar


#admin.site.register(CarBrand)

class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated_at', 'deleted_at')
    list_display_links = ('name', 'id')

admin.site.register(CarBrand, CarBrandAdmin)


class CarModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'car_brand', 'name', 'updated_at', 'deleted_at')
    list_display_links = ('name', 'id')

admin.site.register(CarModel, CarModelAdmin)


class UserCarAdmin(admin.ModelAdmin):
    list_display = (
        'id', 
        'car_brand', 
        'car_model',
        'user', 
        'first_reg', 
        'odometer',
        'updated_at', 
        'deleted_at'
        )
    list_display_links = ('user', 'id')

admin.site.register(UserCar, UserCarAdmin)