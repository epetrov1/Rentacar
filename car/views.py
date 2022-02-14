from . models import CarBrand, CarModel, UserCar
from . serializers import CarBrandSerializer, CarModelSerializer, UserCarSerializer
from rest_framework import viewsets
from rest_framework.response import Response
#from django_filters.rest_framework import DjangoFilterBackend
#from rest_framework.authentication import TokenAuthentication
#from rest_framework.permissions import IsAuthenticated



class CarBrandViewSet(viewsets.ModelViewSet):
    queryset = CarBrand.objects.all()
    serializer_class = CarBrandSerializer
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication, )


    def retrieve(self, request, *args, **kwargs):
        carbrand = CarBrand.objects.filter(name=kwargs['pk'])
        serializer = CarBrandSerializer(carbrand, many=True)
        return Response({"carbrand":serializer.data})




class CarModelViewSet(viewsets.ModelViewSet):
    queryset = CarModel.objects.all()
    serializer_class = CarModelSerializer
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication, )

    def retrieve(self, *args, **kwargs):
        carmodel = CarModel.objects.filter(name=kwargs['pk'])
        serializer = CarModelSerializer(carmodel, many=True)
        return Response({"carmodel": serializer.data})




class UserCarViewSet(viewsets.ModelViewSet):
    queryset = UserCar.objects.all()
    serializer_class = UserCarSerializer
    #permission_classes = [IsAuthenticated]
    #authentication_classes = (TokenAuthentication, )


    def retrieve(self, *args, **kwargs):
        print(kwargs['pk'])
        usercar = UserCar.objects.filter(car_model__name=kwargs['pk'])
        serializer = UserCarSerializer(usercar, many=True)
        return Response({"usercar":serializer.data})

