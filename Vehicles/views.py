from django.shortcuts import render, redirect
import io
import json
import qrcode
from django.http import HttpRequest, JsonResponse,HttpResponse
from .models import VehicleDetails
import base64
from django.shortcuts import get_object_or_404
from datetime import date
from PIL import Image
from io import BytesIO

class CustomJSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, date):
            return obj.isoformat()
        return super().default(obj)

def display_details(request):
    registration_number = request.GET.get('registration_number')
    try:
        vehicle = VehicleDetails.objects.get(registration_number=registration_number)
        return render(request, 'display.html', {'vehicle': vehicle})
    except VehicleDetails.DoesNotExist:
        return render(request, 'home.html', {'message': 'Vehicle not found'})

from django.urls import reverse

def store_vehicle_details(request):
    if request.method == 'POST':
        try:
            # Extract all the form data
            registration_number = request.POST.get('registration_number')
            manufactured_by = request.POST.get('manufactured_by')
            vehicle_model = request.POST.get('vehicle_model')
            year_of_manufacture = request.POST.get('year_of_manufacture')
            body_built_by = request.POST.get('body_built_by')
            type_of_vehicle = request.POST.get('type_of_vehicle')
            battery_size = request.POST.get('battery_size')
            tyre_size = request.POST.get('tyre_size')
            chassis_number = request.POST.get('chassis_number')
            engine_number = request.POST.get('engine_number')
            date_of_delivery = request.POST.get('date_of_delivery')
            order_number = request.POST.get('order_number')
            kgid_policy_number = request.POST.get('kgid_policy_number')
            location = request.POST.get('location')

            # Create a VehicleDetails object
            vehicle = VehicleDetails.objects.create(
                registration_number=registration_number,
                manufactured_by=manufactured_by,
                vehicle_model=vehicle_model,
                year_of_manufacture=year_of_manufacture,
                body_built_by=body_built_by,
                type_of_vehicle=type_of_vehicle,
                battery_size=battery_size,
                tyre_size=tyre_size,
                chassis_number=chassis_number,
                engine_number=engine_number,
                date_of_delivery=date_of_delivery,
                order_number=order_number,
                kgid_policy_number=kgid_policy_number,
                location=location
            )

            display_details_url = reverse('display_details')
            full_url = request.build_absolute_uri(display_details_url)
            qr_data = f"{full_url}?registration_number={registration_number}"
            

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(qr_data)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")

            with io.BytesIO() as output:
                qr_img.save(output)
                image_data = output.getvalue()

            # Convert the image data to a base64 string
            qr_image_base64 = base64.b64encode(image_data).decode()

            data = {
                "qr_image": qr_image_base64,
                "message": "Vehicle details of Vehicle stored successfully!",
                "registration number" : registration_number
            }

            return render(request, 'home.html', data)  # Redirect after successful creation
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'GET Method not allowed'}, status=405)

def home(request):
    if request.method == 'GET':
        return render(request, 'home.html')
    else:
        return redirect('home.html')
    