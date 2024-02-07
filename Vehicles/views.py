from django.shortcuts import render, redirect
from django.http import JsonResponse
from .models import VehicleDetails

def store_vehicle_details(request):
    if request.method == 'POST':
        try:
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

            # Create a new VehicleDetails object
            vehicle = VehicleDetails(
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
                kgid_policy_number=kgid_policy_number
            )
            vehicle.save()  # Save the object to the database
            return redirect('home') #Could not redirect with a message parameter for home.html!
        
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    
    else:
        return JsonResponse({'error': 'GET Method not allowed'}, status=405)



def home(request):

    message = request.GET.get('message',None)
    return render(request, 'home.html', {'message':message})

