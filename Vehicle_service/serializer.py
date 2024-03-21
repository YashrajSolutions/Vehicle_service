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


class vehicle_details_by_date_range_serializer(serializers.ModelSerializer):
    class Meta:
        model = vehicle_details
        fields = ('vin_no','registration_no','address','user_id','fuel_type','vehicle_type','emission_nom','engine_no')



class VehicleDetailsSerializer(serializers.ModelSerializer):
    fuel_type_name = serializers.SerializerMethodField()
    vehicle_type_name = serializers.SerializerMethodField()
    emission_nom_name = serializers.SerializerMethodField()

    class Meta:
        model = vehicle_details
        fields = ['vin_no','registration_no','address','user_id','engine_no', 'fuel_type', 'vehicle_type', 'emission_nom', 'fuel_type_name', 'vehicle_type_name', 'emission_nom_name','making_date','is_onboard']

    def get_fuel_type_name(self, obj):
        return fuel_types.objects.get(id=obj.fuel_type).name

    def get_vehicle_type_name(self, obj):
        return vehicle_types.objects.get(id=obj.vehicle_type).name

    def get_emission_nom_name(self, obj):
        return emission_nom.objects.get(id=obj.emission_nom).name