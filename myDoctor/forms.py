from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    first_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    last_name = forms.CharField(
        widget=forms.TextInput(attrs={'class':'form-control'}),
    )
    class Meta:
        model = Appointment
        fields = ['request', 'phone']
        
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)

        # self.fields['first_name'].widget.attrs['class'] = 'form-control'
        # self.fields['last_name'].widget.attrs['class'] = 'form-control'
        # self.fields['email'].widget.attrs['class'] = 'form-control'
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['request'].widget.attrs['class'] = 'form-control'