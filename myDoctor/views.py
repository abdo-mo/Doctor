from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse
from .forms import AppointmentForm, AppointmentUpdateForm, AppointmentRescheduleForm
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
            appointment.patient = request.user
            appointment.save()
        return redirect('appointmentsList')
    else:
        form = AppointmentForm()
    context['form'] = form
    return render(request, 'new_appointment.html', context)

def appointmentsList(request):
    appointments = Appointment.objects.all()
    return render(request, 'appointments.html', {'appointments': appointments})

def appointmentUpdate(request, id):
    context = {}
    obj = get_object_or_404(Appointment, id=id)
    form = AppointmentUpdateForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('appointmentsList')
    context['form'] = form
    return render(request, 'appointmentUpdate.html', context)

def appointmentReschedule(request, id):
    context = {}
    obj = get_object_or_404(Appointment, id=id)
    form = AppointmentRescheduleForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('home')
    context["form"] = form
    return render(request, 'appointmentReschedule.html', context)

def conformDelete(request, id):
    context = {}
    obj = get_object_or_404(Appointment, id=id)
    context['obj'] = obj
    return render(request, 'conformDelete.html', context)
def delete(request, id):
    obj = get_object_or_404(Appointment, id=id)
    obj.delete()
    return redirect('appointmentsList')
