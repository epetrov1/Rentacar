from . models import CarBrand, CarModel, UserCar
from rest_framework import viewsets
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated
from . serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer



class CarBrandViewSet(viewsets.ModelViewSet):
    
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication, )


class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    #permission_classes = [IsAuthenticated]


class UserCarViewSet(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    #permission_classes = [IsAuthenticated]