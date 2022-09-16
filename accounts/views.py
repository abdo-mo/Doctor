from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import *
from .models import User, Patients

# Create your views here.

def signup(request):
    user_form = SignUpForm()
    patient_form = PatientForm()
    if request.method == "POST":
        user_form = SignUpForm(request.POST)
        patient_form = PatientForm(request.POST)
        if user_form.is_valid() and patient_form.is_valid():            
            user = user_form.save(commit=False)
            user.is_doctor = False
            user.is_patient = True
            user = user_form.save()
            patient = patient_form.save(commit=False)
            patient.user = user
            patient.gender = patient_form.cleaned_data.get('gender')
            patient.job = patient_form.cleaned_data.get('job')
            patient.save()
            return redirect('home')
        else:
            print('it is validation error')
    return render(request, 'signup.html', {'user_form':user_form, 'patient_form': patient_form})

# class patientSignUpView(CreateView):
#     model = User
#     form_class = patientSignUpForm
#     template_name = 'registration/signup_form.html'

#     def get_context_data(self, **kwargs):
#         kwargs['user_type'] = 'student'
#         return super().get_context_data(**kwargs)

#     def form_valid(self, form):
#         user = form.save()
#         login(self.request, user)
#         return redirect('students:quiz_list')
