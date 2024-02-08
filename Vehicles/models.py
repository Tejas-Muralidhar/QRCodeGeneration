from django.db import models

class VehicleDetails(models.Model):
    registration_number = models.CharField(max_length=20, primary_key=True)
    manufactured_by = models.CharField(max_length=50)
    vehicle_model = models.CharField(max_length=50)
    year_of_manufacture = models.IntegerField()
    body_built_by = models.CharField(max_length=50)
    type_of_vehicle = models.CharField(max_length=50)
    battery_size = models.CharField(max_length=20)
    tyre_size = models.CharField(max_length=20)
    chassis_number = models.CharField(max_length=30)
    engine_number = models.CharField(max_length=30)
    date_of_delivery = models.DateField()
    order_number = models.CharField(max_length=20)
    kgid_policy_number = models.CharField(max_length=30)
    location = models.CharField(max_length=45)

class VehicleQR(models.Model):
    registration_number = models.ForeignKey(VehicleDetails, on_delete=models.CASCADE, primary_key = True,)
    image_blob = models.BinaryField()
