from django.contrib import admin

from main_app.models import Patient , Doctor, Appointment, Department, Bed , Medication, Test, Procedure, Billing , Nurse, Ward ,Shift , Admission, Discharge

# Register your models here.


@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'age')
    list_per_page = 25


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = ('name','specialization')
    list_per_page = 25


@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display =('patient','doctor')
    list_per_page = 25


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ('name','description')
    list_per_page = 25



@admin.register(Bed)
class BedAdmin(admin.ModelAdmin):
    list_display = ('department','patient', 'number', 'is_occupied', 'bed_type','ward')
    list_per_page = 25


@admin.register(Medication)
class MedicationAdmin(admin.ModelAdmin):
    list_display = ('name', 'dosage')
    list_per_page = 25


@admin.register(Test)
class TestAdmin(admin.ModelAdmin):
    list_display = ('name', 'result')
    list_per_page = 25


@admin.register(Procedure)
class ProcedureAdmin(admin.ModelAdmin):
    list_display = ('name', 'performing_doctor')
    list_per_page = 25
    

@admin.register(Billing)
class BillingAdmin(admin.ModelAdmin):
    list_display =('amount','date_time')
    list_per_page = 25

@admin.register(Nurse)
class NurseAdmin(admin.ModelAdmin):
    list_display =('name', 'role')
    list_per_page = 25


@admin.register(Ward)
class WardAdmin(admin.ModelAdmin):
    list_display = ('name', 'capacity')

@admin.register(Shift)
class ShiftAdmin(admin.ModelAdmin):
    list_display = ('nurse', 'start_time', 'end_time', 'department')
    list_per_page = 25


@admin.register(Admission)
class AdmissionAdmin(admin.ModelAdmin):
    list_display = ('patient', 'admission_date_time')
    list_per_page = 25

@admin.register(Discharge)
class DischargeAdmin(admin.ModelAdmin):
     list_display = ('admission', 'reason')
     list_per_page = 25


