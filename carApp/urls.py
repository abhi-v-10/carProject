from django.urls import path
from . import views

urlpatterns = [
    path('get_all_cars/', views.get_all_cars, name='get_all_cars'),
    path('get_car/<int:id>/', views.get_car, name='get_car'),
    path('post_car/', views.post_car, name='post_cas'),
    path('update_car/<int:id>/', views.update_car, name='update_car'),
    path('delete_car/<int:id>/', views.delete_car, name='delete_car'),
    path('get_manufacturer/', views.get_manufacturer, name='get_manufacturer'),
    path('get_feature/', views.get_feature, name='get_feature'),
    path('get_engine/', views.get_engine, name='get_engine'), 
]