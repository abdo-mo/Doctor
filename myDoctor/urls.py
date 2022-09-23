from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeView, name = 'home'),
    path('appointment/new/', views.newAppointment, name='newAppointment'),
    path('appointment/list/', views.appointmentsList, name='appointmentsList'),
    path('appointment/<int:id>/update', views.appointmentUpdate, name='appointmentUpdate'),
    path('appointment/<int:id>/reschedule', views.appointmentReschedule, name='appointmentReschedule'),
    path('appointment/<int:id>/delete', views.delete, name="delete"),
    path('appointment/<int:id>/conformDelete', views.conformDelete, name='conformDelete'),
]
