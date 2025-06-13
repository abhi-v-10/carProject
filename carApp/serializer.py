from rest_framework import serializers
from .models import *

class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        exclude = ['id']
        

class ManufacturerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Manufacturer
        exclude = ['id']
        

class FeatureSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feature
        exclude = ['id']


class CarsSerializer(serializers.ModelSerializer):
    engine = EngineSerializer(required=False)
    manufacturer = ManufacturerSerializer(required=False)
    features = FeatureSerializer(many=True, required=False)
    
    class Meta: 
        model = Cars
        exclude = ['id']

    def validate_price(self, value):
        if value < 0:
            raise serializers.ValidationError("Price cannot be negative.")
        return value    
        
    def validate_fuel(self, value):
        valid_fuels = ['Petrol', 'Diesel', 'Electric', 'Hybrid']
        if value not in valid_fuels:
            raise serializers.ValidationError(f"Fuel type must be one of {valid_fuels}.")
        return value

    def validate(self, data):
        if not data.get('company'):
            raise serializers.ValidationError("Company name is required.")
        if not data.get('model'):
            raise serializers.ValidationError("Model name is required.")
        return data

    