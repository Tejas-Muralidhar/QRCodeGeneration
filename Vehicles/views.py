from django.shortcuts import render, redirect
import io
import json
import qrcode
from django.http import JsonResponse
from .models import VehicleDetails, VehicleQR
import base64

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

            # Create a dictionary with all the data
            vehicle_data = {
                'registration_number': registration_number,
                'manufactured_by': manufactured_by,
                'vehicle_model': vehicle_model,
                'year_of_manufacture': year_of_manufacture,
                'body_built_by': body_built_by,
                'type_of_vehicle': type_of_vehicle,
                'battery_size': battery_size,
                'tyre_size': tyre_size,
                'chassis_number': chassis_number,
                'engine_number': engine_number,
                'date_of_delivery': date_of_delivery,
                'order_number': order_number,
                'kgid_policy_number': kgid_policy_number,
                'location': location
            }

            # Serialize the dictionary to JSON
            vehicle_data_json = json.dumps(vehicle_data)

            # Generate QR code
            qr = qrcode.QRCode(
                version=1,
                error_correction=qrcode.constants.ERROR_CORRECT_L,
                box_size=10,
                border=4,
            )
            qr.add_data(vehicle_data_json)
            qr.make(fit=True)
            qr_img = qr.make_image(fill_color="black", back_color="white")

            # Save QR code image as binary data
            with io.BytesIO() as output:
                qr_img.save(output)
                qr_image_blob = output.getvalue()

            # Create a VehicleQR object and save QR code blob
            vehicle_qr = VehicleQR.objects.create(
                registration_number=vehicle,
                image_blob=qr_image_blob
            )

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
    return render(request, 'home.html')

