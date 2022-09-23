from django import forms
from .models import Appointment

class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['request', 'phone', 'do_date']
        widgets = {
            'do_date' : forms.DateInput()
        }
        
    def __init__(self, *args, **kwargs):
        super(AppointmentForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['request'].widget.attrs['class'] = 'form-control'
        self.fields['do_date'].widget.attrs['class'] = 'form-control'

class AppointmentUpdateForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['request', 'phone']
        
    def __init__(self, *args, **kwargs):
        super(AppointmentUpdateForm, self).__init__(*args, **kwargs)
        self.fields['phone'].widget.attrs['class'] = 'form-control'
        self.fields['request'].widget.attrs['class'] = 'form-control'

class AppointmentRescheduleForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = ['do_date']
        widgets = {
            'do_date': forms.DateInput()
        }
        
    def __init__(self, *args, **kwargs):
        super(AppointmentRescheduleForm, self).__init__(*args, **kwargs)
        self.fields['do_date'].widget.attrs['class'] = 'form-control'
        