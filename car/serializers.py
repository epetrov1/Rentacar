from rest_framework import serializers
from .models import CarBrand, CarModel, UserCar

class CarBrandSerializer(serializers.Serializer):
    class Meta:
        model = CarBrand
        fields = (
            'id', 
            'name',
            'created_at', 
            'updated_at', 
            'deleted_at'
            )



class CarModelSerializer(serializers.Serializer):
    class Meta:
        model = CarModel
        fields = (
            'id', 
            'name', 
            'car_brand', 
            'created_at', 
            'updated_at', 
            'deleted_at'
            )


class UserCarSerializer(serializers.Serializer):
    class Meta:
        model = UserCar
        fields = (
            'id', 
            'name', 
            'car_brand', 
            'car_model', 
            'odometer', 
            'first_reg',
            'created_at',
            'updated_at', 
            'deleted_at'
            )