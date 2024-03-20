from rest_framework import serializers
from .models import vehicle_details, fuel_types, vehicle_types, emission_nom

class fuel_type_serializer(serializers.ModelSerializer):
    class Meta:
        model = fuel_types
        fields = '__all__'

class vehicle_types_serializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle_types
        fields = '__all__'

class emission_nom_serializer(serializers.ModelSerializer):
    class Meta:
        model = emission_nom
        fields = '__all__'

class vehicle_details_serializer(serializers.ModelSerializer):
    fuel_type = fuel_type_serializer()
    vehicle_type = vehicle_types_serializer()
    emission_nom = emission_nom_serializer()
    class Meta:
        model = vehicle_details
        fields = '__all__'

class vehicle_details_serializer_2(serializers.ModelSerializer):
    class Meta:
        model = vehicle_details
        fields = '__all__'


