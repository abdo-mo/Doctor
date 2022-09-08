from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import AppointmentForm

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
            appointment.patient = request.user
            appointment.save()
        return redirect('home')
    else:
        form = AppointmentForm()
    context['form'] = form
    return render(request, 'new_appointment.html', context)