from django.contrib.auth.forms import UserCreationForm
from django import forms
# from django.contrib.auth.models import User
from .models import Patients, User

# class PatientSignUpForm(UserCreationForm):
#     password1 = forms.CharField(
#         label="Password",
#         widget=forms.PasswordInput(attrs={'class':'form-control'}),
#     )
#     password2 = forms.CharField(
#         label="Confirm password",
#         widget=forms.PasswordInput(attrs={'class':'form-control'}),
#     )
    
#     class Meta:
#         widgets = {
#             'user': forms.TextInput(attrs={'class': 'form-control'}),
#             'email': forms.EmailInput(attrs={'class': 'form-control'}),
#          }
#         model = Patients
#         fields = ('user', 'password1', 'password2', 'gender', 'job')

class PatientForm(forms.ModelForm):
    username = forms.CharField(
        label="User Name",
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    password1 = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={'class':'form-control'}),
    )
    
    class Meta:
        model = Patients
        fields = ('username', 'email', 'password1', 'password2', 'gender', 'job')
        GENDER_CHOICES = [('Male', 'Male'), ('Female', 'Female')]
        widgets = {
                    'gender': forms.Select(choices=GENDER_CHOICES,attrs={'class': 'form-control'}),
                }
    email = forms.CharField(max_length=255, required=True, widget=forms.EmailInput(attrs={'class': 'form-control'}))



# class UserUpdateForm(forms.ModelForm):
#     email = forms.EmailField()

#     class Meta:
#         model = User
#         fields = ['username', 'email']

#     def __init__(self, *args, **kwargs):
#         super(UserUpdateForm, self).__init__(*args, **kwargs)
#         self.fields['username'].widget.attrs.update({'class': 'form-control'})
#         self.fields['email'].widget.attrs.update({'class': 'form-control mb-3'})

# class ProfileUpdateForm(forms.ModelForm):
#     class Meta:
#         model = Profile
#         fields = ['image']

