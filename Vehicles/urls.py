from django.urls import path
from .views import store_vehicle_details,home,get_vehicle_qr_image,render_get_qr

urlpatterns = [
    path('',home, name='home'),
    path('store-vehicle/',store_vehicle_details,name='store-vehicle'),
    path('get-qr/',get_vehicle_qr_image,name="get-qr"),
    path('get-registered',render_get_qr,name="fetch")
]
