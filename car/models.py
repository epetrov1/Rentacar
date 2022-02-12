from pyexpat import model
from django.db import models
from django.utils import timezone
from datetime import datetime
from django.contrib.auth import get_user_model
User = get_user_model()


class SoftDeleteManager(models.Manager):

    def get_queryset(self):
        return super().get_queryset().filter(deleted_at__isnull=True)


class SoftDeleteModel(models.Model):

    deleted_at = models.DateTimeField(blank=True, default=None)
    undeleted_objects = models.Manager()
    objects = SoftDeleteManager()

    def soft_delete(self):
        self.deleted_at = timezone.now()
        self.save()

    def restore(self):
        self.deleted_at = None
        self.save()

    class Meta:
        abstract = True


class CarBrand(SoftDeleteModel):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    name = models.CharField(max_length=255)


class CarModel(SoftDeleteModel):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    name = models.CharField(max_length=255)


class UserCar(SoftDeleteModel):
    created_at = models.DateTimeField(auto_now_add= True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    car_brand = models.ForeignKey(CarBrand, on_delete=models.CASCADE)
    car_model = models.ForeignKey(CarModel, on_delete= models.CASCADE)
    first_reg = models.CharField(max_length=10)
    odometer = models.IntegerField()

