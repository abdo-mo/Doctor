from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppointmentForm
from .models import Appointment

# Create your views here.

def homeView(request):
    return render(request, 'index.html', )

    # return HttpResponse('hiii')
def newAppointment(request):
    
    context = {}

    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            appointment = form.save(commit=False)
            user = request.user
            user.first_name = form.cleaned_data['first_name']
            user.last_name = form.cleaned_data['last_name']
            user.save()
            appointment.patient = user
            appointment.save()
        return redirect('home')
    else:
        form = AppointmentForm()
    context['form'] = form
    return render(request, 'new_appointment.html', context)

def appointmentsList(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})