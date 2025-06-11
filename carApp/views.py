from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from .serializer import CarsSerializer

# Create your views here.
@api_view(['GET'])
def get_all_cars(request):
    company = request.query_params.get('company', None)
    fuel = request.query_params.get('fuel', None)
    car = Cars.objects.all()
    if company:
        car = car.filter(company__icontains=company)
    elif fuel:
        car = car.filter(fuel__icontains=fuel)        

    serializer = CarsSerializer(car, many=True)
    return Response({'cars': serializer.data}, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_car(request, id):
    try:
        car = Cars.objects.get(id=id)
        serializer = CarsSerializer(car)
        return Response({'car': serializer.data}, status=status.HTTP_200_OK)
    except Cars.DoesNotExist:
        return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def filter_car(request):
    fuel = request.query_params.get('fuel', None)
    price = request.query_params.get('price', None)
    
    if fuel:
        cars = Cars.objects.filter(fuel=fuel)
    elif price:
        cars = Cars.objects.filter(price__lte=price)
    else:
        cars = Cars.objects.all()
    
    serializer = CarsSerializer(cars, many=True)
    return Response({'cars': serializer.data}, status=status.HTTP_200_OK)


@api_view(['POST'])
@permission_classes([AllowAny])
def post_car(request):
    data = request.data
    serializer = CarsSerializer(data=data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Car posted successfully', 'car': serializer.data}, status=status.HTTP_201_CREATED)
    return Response({'error': 'Failed to post car'}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT', 'PATCH'])
@permission_classes([AllowAny])
def update_car(request, id):
    try:
        car = Cars.objects.get(id=id)
    except Cars.DoesNotExist:
        return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = CarsSerializer(car, data=request.data, partial=True)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Car updated successfullu', 'car': serializer.data}, status=status.HTTP_200_OK)
    else:
        return Response({'error': serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([AllowAny])
def delete_car(request, id):
    try:
        car = Cars.objects.get(id=id)
        car.delete()
        return Response({'message': 'Car deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
    except Cars.DoesNotExist:
        return Response({'error': 'Car not found'}, status=status.HTTP_404_NOT_FOUND)




