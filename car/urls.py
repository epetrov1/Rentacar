from django.urls import include, path, re_path
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register('carbrand', views.CarBrandViewSet, basename = 'carbrand')
router.register('carmodel', views.CarModelViewSet, basename = 'carmodel')
router.register('usercar', views.UserCarViewSet, basename = 'usercar')

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    path('', include(router.urls)),
]