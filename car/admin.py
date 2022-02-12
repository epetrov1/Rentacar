from django.contrib import admin
from . models import CarBrand, CarModel, UserCar


#admin.site.register(CarBrand)

class CarBrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'updated_at', 'deleted_at')
    list_display_links = ('name', 'id')

admin.site.register(CarBrand, CarBrandAdmin)