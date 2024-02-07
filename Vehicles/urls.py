from django.urls import path
from .views import store_vehicle_details,home

urlpatterns = [
    path('',home, name='home'),
    path('store-vehicle/',store_vehicle_details,name='store-vehicle')
]
