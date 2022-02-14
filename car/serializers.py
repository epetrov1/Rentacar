from rest_framework import serializers
from .models import CarBrand, CarModel, UserCar

class CarBrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarBrand
        fields = [
            'id', 
            'name',
            'created_at', 
            'updated_at', 
            'deleted_at'
        ]



class CarModelSerializer(serializers.ModelSerializer):
    car_brand = serializers.PrimaryKeyRelatedField(read_only=True)
    class Meta:
        model = CarModel
        fields = [
            'id', 
            'name', 
            'car_brand', 
            'created_at', 
            'updated_at', 
            'deleted_at'
        ]


class UserCarSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCar
        fields = [
            'id', 
            'user', 
            'car_brand', 
            'car_model', 
            'odometer', 
            'first_reg',
            'created_at',
            'updated_at', 
            'deleted_at'
        ]