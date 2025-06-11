from django.urls import path
from . import views

urlpatterns = [
    path('get_all_cars/', views.get_all_cars, name='get_all_cars'),
    path('get_car/<int:id>/', views.get_car, name='get_car'),
    path('post_car/', views.post_car, name='post_cas'),
    path('update_car/<int:id>/', views.update_car, name='update_car'),
    path('delete_car/<int:id>/', views.delete_car, name='delete_car'),
]