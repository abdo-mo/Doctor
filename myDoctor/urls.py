from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeView, name = 'home'),
    path('appointment/new/', views.newAppointment, name='newAppointment')
]
