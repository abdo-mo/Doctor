from django.shortcuts import render, redirect
from django.views.generic import CreateView
from .forms import *
from .models import User, PatientMore

# Create your views here.

def signup(request):
    form = PatientSignUpForm()
    print('test')
    if request.method == "POST":
        form = PatientSignUpForm(request.POST)
        print('test again')
        if form.is_valid():
            print('test adding user')
            patient = form.save()
            patientMore = PatientMore.objects.create(
                gender = form.cleaned_data.get('gender'),
                job = form.cleaned_data.get('job'),
                user = patient
            )
            print('done', form)
            return redirect('home')
        else:
            print('it is validation error')
    return render(request, 'signup.html', {'form':form})

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
