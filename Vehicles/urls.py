from django.urls import path
from .views import store_vehicle_details,home,display_details

urlpatterns = [
    path('',home, name='home'),
    path('store-vehicle/',store_vehicle_details,name='store-vehicle'),
    path('display-details/',display_details,name="display_details"),
]
