from django.urls import path
from .import views

urlpatterns = [
    path('', views.homeView, name = 'home'),
    path('appointment/new/', views.newAppointment, name='newAppointment'),
    path('appointment/list/', views.all_appointmentsList, name='all_appointmentsList'),
    path('appointment/comming/', views.comming_appointments, name='comming_appointments'),
    path('appointment/<int:id>/update', views.appointmentUpdate, name='appointmentUpdate'),
    path('appointment/<int:id>/reschedule', views.appointmentReschedule, name='appointmentReschedule'),
    path('appointment/<int:id>/delete', views.delete, name="delete"),
    path('appointment/<int:id>/conformDelete', views.conformDelete, name='conformDelete'),
]
