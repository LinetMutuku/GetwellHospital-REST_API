from django import forms
from .models import Patient , Doctor, Appointment, Nurse, Ward , Billing , Bed, Medication

class LoginForm(forms.Form):
    username = forms.CharField(max_length=60)
    password = forms.CharField(max_length=60, widget=forms.PasswordInput)
    email = forms.EmailField(max_length=100, widget=forms.EmailInput, label='Email Address')



class PatientForm(forms.ModelForm):
    class Meta:
        model = Patient 
        fields = '__all__'


class DoctorForm(forms.ModelForm):
    class Meta:
        model = Doctor
        fields = '__all__'


class AppointmentForm(forms.ModelForm):
    class Meta:
        model = Appointment
        fields = '__all__' 


class NurseForm(forms.ModelForm):
    class Meta:
        model = Nurse  # Specify the model here
        fields = '__all__' 



class WardForm(forms.ModelForm):
    class Meta:
        model = Ward
        fields =  '__all__'


class BillingForm(forms.ModelForm):
    class Meta:
        model = Billing
        fields =  '__all__'


class BedForm(forms.ModelForm):
    class Meta:
        model = Bed
        fields =  '__all__'


class MedicationForm(forms.ModelForm):
    class Meta:
        model = Medication
        fields =  '__all__'