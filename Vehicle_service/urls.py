"""
URL configuration for Vehicle_service project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    #Vehicle Service
    path('api/vehicle-service/create', views.create_vehicle, name='create_vehicle'),
    path('apk/vehicle-service/pk=<int:pk>', views.read_vehicle, name='read_vehicle'),
    path('api/vehicle-service/<int:pk>/update', views.update_vehicle, name='update_vehicle'),
    path('api/vehicle-service', views.get_all_vehicle_list, name='get_all_vehicle_list'),
    path('api/vehicle_service/<int:pk>/delete', views.delete_vehicle, name='delete_vehicle'),

    # URLs for fuel types
    path('api/fuel-type/create', views.create_fuel_type, name='create_fuel_type'),
    path('api/fuel-type/<int:pk>', views.read_fuel_type, name='read_fuel_type'),
    path('api/fuel-type/<int:pk>/update', views.update_fuel_type, name='update_fuel_type'),
    path('api/fuel-type', views.get_all_fuel_list, name='get_all_fuel_list'),
    path('api/fuel-type/<int:pk>/delete', views.delete_fuel_type, name='delete_fuel_type'),
    
    # URLs for vehicle types
    path('api/vehicle-type/create', views.create_vehicle_type, name='create_vehicle_type'),
    path('api/vehicle-type/<int:pk>', views.read_vehicle_type, name='read_vehicle_type'),
    path('api/vehicle-type/<int:pk>/update', views.update_vehicle_type, name='update_vehicle_type'),
    path('api/vehicle-type', views.get_all_vehicle_type_list, name='get_all_vehicle_type_list'),
    path('api/vehicle-type/<int:pk>/delete', views.delete_vehicle_type, name='delete_vehicle_type'),
    
    # URLs for emission nominal
    path('api/emission-nom/create', views.create_emission_nom, name='create_emission_nom'),
    path('api/emission-nom/<int:pk>', views.read_emission_nom, name='read_emission_nom'),
    path('api/emission-nom/<int:pk>/update', views.update_emission_nom, name='update_emission_nom'),
    path('api/emission-nom', views.get_all_emission_nom_list, name='get_all_emission_list'),
    path('api/emission-nom/<int:pk>/delete', views.delete_emission_nom, name='delete_emission_nom'),

    #InterService call for vehicle details by date
    path('api/vehicle-service/details-by-date/', views.get_vehicle_details_by_date, name='vehicle_details_by_date'),
    path('api/vehicle-service/details-by-id/', views.get_vehicle_details_by_id, name='vehicle_details_by_id')

]
