from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import vehicle_details,fuel_types,vehicle_types,emission_nom
from .serializer import vehicle_details_serializer,fuel_type_serializer,vehicle_types_serializer,emission_nom_serializer,vehicle_details_serializer_2
import time 
from functools import wraps
from rest_framework.decorators import api_view

def measure_execution_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Execution time of {func.__name__}: {execution_time:.4f} seconds")
        return result
    return wrapper


# For Vehicle Details ----------------------------------------------------------------------------------

@csrf_exempt
@measure_execution_time
def create_vehicle(request):
    try:
        if request.method == "POST":
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
            
            serializer = vehicle_details_serializer_2(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle created successfully!!", "data": serializer.data}, status=201)
            else:
                return JsonResponse({"message": "Invalid Data Provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid Http Method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)

@csrf_exempt
@measure_execution_time
def read_vehicle(request, pk):
    try:
        vehicle_object = vehicle_details.objects.get(pk=pk, is_deleted=False)
        serializer = vehicle_details_serializer(vehicle_object)
        return JsonResponse({"message": "Vehicle details retrieved successfully!!", "data": serializer.data})
    except vehicle_details.DoesNotExist:
        return JsonResponse({"message": "Vehicle not found!!"}, status=404)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
@csrf_exempt
@measure_execution_time
def get_all_vehicle_list(request):
    try:
        vehicle_object = vehicle_details.objects.filter(is_deleted=False)
        serializer = vehicle_details_serializer(vehicle_object, many=True)
        if serializer.data:
            return JsonResponse({"message":"Vehicle details retrieved successfully!!","total":len(serializer.data),"data":serializer.data})
        else:
            return JsonResponse({"message":"No data found!!"})
    except Exception as error:
        print("get_all_vehicle_list(): ", error)
        return JsonResponse({"message":"Something went wrong"},status=500)

@csrf_exempt
@measure_execution_time
def update_vehicle(request, pk):
    try:
        vehicle_object = vehicle_details.objects.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request
            
            serializer = vehicle_details_serializer(vehicle_object, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)

@csrf_exempt
@measure_execution_time
def delete_vehicle(request, pk):
    try:
        vehicle = vehicle_details.objects.get(pk=pk)
        if request.method == 'DELETE':
            vehicle.delete()
            return JsonResponse({"message": "Vehicle deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


# For Fuel Type--------------------------------------------------------------------------------------
     
@csrf_exempt
@measure_execution_time
def create_fuel_type(request):
    try:
        if request.method == "POST":
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request

            serializer = fuel_type_serializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Fuel type created successfully!!", "data": serializer.data},
                                    status=201)
            else:
                return JsonResponse({"message": "Invalid Data Provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid Http Method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    

@csrf_exempt
@measure_execution_time
def read_fuel_type(request, pk):
    try:
        fuel_type = fuel_types.objects.get(pk=pk)
        serializer = fuel_type_serializer(fuel_type)
        return JsonResponse({"message": "Fuel type details retrieved successfully!!", "data": serializer.data})
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
@measure_execution_time
def update_fuel_type(request, pk):
    try:
        fuel_type = fuel_types.objects.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request

            serializer = fuel_type_serializer(fuel_type, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Fuel type updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
@csrf_exempt
@measure_execution_time
def get_all_fuel_list(request):
    try:
        fuel_object = fuel_types.objects.filter(is_deleted=False)
        serializer = fuel_type_serializer(fuel_object, many=True)
        if serializer.data:
            return JsonResponse({"message":"Fuel Types retrieved successfully!!","total":len(serializer.data),"data":serializer.data})
        else:
            return JsonResponse({"message":"No data found!!"})
    except Exception as error:
        print("get_all_fuel_list(): ", error)
        return JsonResponse({"message":"Something went wrong"},status=500)


@csrf_exempt
@measure_execution_time
def delete_fuel_type(request, pk):
    try:
        fuel_type = fuel_types.objects.get(pk=pk)
        if request.method == 'DELETE':
            fuel_type.delete()
            return JsonResponse({"message": "Fuel type deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


# For Vehicle Type-------------------------------------------------------------------------------------
    
@csrf_exempt
@measure_execution_time
def create_vehicle_type(request):
    try:
        if request.method == "POST":
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request

            serializer = vehicle_types_serializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle type created successfully!!", "data": serializer.data},
                                    status=201)
            else:
                return JsonResponse({"message": "Invalid Data Provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid Http Method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
@measure_execution_time
def read_vehicle_type(request, pk):
    try:
        vehicle_type = vehicle_types.objects.get(pk=pk)
        serializer = vehicle_types_serializer(vehicle_type)
        return JsonResponse({"message": "Vehicle type details retrieved successfully!!", "data": serializer.data})
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
@measure_execution_time
def update_vehicle_type(request, pk):
    try:
        vehicle_type = vehicle_types.objects.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request

            serializer = vehicle_types_serializer(vehicle_type, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Vehicle type updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
@measure_execution_time
def get_all_vehicle_type_list(request):
    try:
        vehicle_type_object = vehicle_types.objects.filter(is_deleted=False)
        serializer = vehicle_types_serializer(vehicle_type_object, many=True)
        if serializer.data:
            return JsonResponse({"message":"Fuel Types retrieved successfully!!","total":len(serializer.data),"data":serializer.data})
        else:
            return JsonResponse({"message":"No data found!!"})
    except Exception as error:
        print("get_all_vehicle_type_list(): ", error)
        return JsonResponse({"message":"Something went wrong"},status=500)


@csrf_exempt
@measure_execution_time
def delete_vehicle_type(request, pk):
    try:
        vehicle_type = vehicle_types.objects.get(pk=pk)
        if request.method == 'DELETE':
            vehicle_type.delete()
            return JsonResponse({"message": "Vehicle type deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


# For Emission_nom --------------------------------------------------------------------------------

@csrf_exempt
@measure_execution_time
def create_emission_nom(request):
    try:
        if request.method == "POST":
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request

            serializer = emission_nom_serializer(data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Emission nominal created successfully!!", "data": serializer.data},
                                    status=201)
            else:
                return JsonResponse({"message": "Invalid Data Provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid Http Method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


@csrf_exempt
@measure_execution_time
def read_emission_nom(request, pk):
    try:
        emission_nominal = emission_nom.objects.get(pk=pk)
        serializer = emission_nom_serializer(emission_nominal)
        return JsonResponse({"message": "Emission nominal details retrieved successfully!!", "data": serializer.data})
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
@csrf_exempt
@measure_execution_time
def update_emission_nom(request, pk):
    try:
        emission_object = emission_nom.objects.get(pk=pk)
        if request.method == 'PUT':
            if type(request) != dict:
                request_data = json.loads(request.body)
            else:
                request_data = request

            serializer = emission_nom_serializer(emission_object, data=request_data)
            if serializer.is_valid():
                serializer.save()
                return JsonResponse({"message": "Emission Nom updated successfully!!!", "data": serializer.data})
            else:
                return JsonResponse({"message": "Invalid data provided", "errors": serializer.errors}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)
    
@csrf_exempt
@measure_execution_time
def get_all_emission_nom_list(request):
    try:
        emission_object = emission_nom.objects.filter(is_deleted=False)
        serializer = emission_nom_serializer(emission_object, many=True)
        if serializer.data:
            return JsonResponse({"message":"Emission Nominal retrieved successfully!!","total":len(serializer.data),"data":serializer.data})
        else:
            return JsonResponse({"message":"No data found!!"})
    except Exception as error:
        print("get_all_emission_list(): ", error)
        return JsonResponse({"message":"Something went wrong"},status=500)


@csrf_exempt
@measure_execution_time
def delete_emission_nom(request, pk):
    try:
        emission_object = emission_nom.objects.get(pk=pk)
        if request.method == 'DELETE':
            emission_nom.delete()
            return JsonResponse({"message": "Emission Nom deleted successfully!!!"})
        else:
            return JsonResponse({"message": "Invalid HTTP method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


# Inter-Service Call for vehicle onboarding on date given
    
from django.utils.dateparse import parse_date

@csrf_exempt
def get_vehicle_details_by_date(request):
    try:
        if request.method == "GET":
            date_str = request.GET.get('date')  
            if date_str:
                date_obj = parse_date(date_str)
                if date_obj:
                    vehicle_objects = vehicle_details.objects.filter(created_at__date=date_obj, is_deleted=False)
                    serializer = vehicle_details_serializer(vehicle_objects, many=True)
                    if serializer.data:
                        return JsonResponse({"message": f"Vehicle details for date {date_obj} retrieved successfully!!", "data": serializer.data})
                    else:
                        return JsonResponse({"message": f"No vehicle details found for date {date_obj}"})
                else:
                    return JsonResponse({"message": "Invalid date format. Please provide date in YYYY-MM-DD format."}, status=400)
            else:
                return JsonResponse({"message": "Date parameter is missing."}, status=400)
        else:
            return JsonResponse({"message": "Invalid HTTP Method"}, status=405)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)


# Inter-Service Call for vehicle by user_id

def parse_user_id(user_id):
    try:
        parsed_user_id = int(user_id)
        return parsed_user_id   
    except ValueError:
        return None




@api_view(['GET'])
@csrf_exempt
def get_vehicle_details_by_id(request):
    try:
        user_obj = request.GET.get('user_id')  
        if user_obj:
            vehicle_objects = vehicle_details.objects.filter(user_id=user_obj, is_deleted=False)
            serializer = vehicle_details_serializer(vehicle_objects, many=True)
            if serializer.data:
                return JsonResponse({"message": f"Vehicle details for id {user_obj} retrieved successfully!!", "data": serializer.data})
            else:
                return JsonResponse({"message": f"No vehicle details found for date {user_obj}"})
        else:
            return JsonResponse({"message": "Invalid User format."}, status=400)
    except Exception as error:
        return JsonResponse({"message": "Something went wrong", "error": str(error)}, status=500)   