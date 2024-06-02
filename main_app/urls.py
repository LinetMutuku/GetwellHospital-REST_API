from . import api_views
from . import views
from django.urls import path
urlpatterns = [

        # urls for the fronted view
    path('',views.getwellpage, name = 'getwellpage'),
    path('signin', views.signin, name='signin'),
    path('home', views.home, name='home'),
    path('view_patients', views.view_patients, name='view_patients'),
    path('patient_details/<int:patient_id>/', views.patient_details, name='patient_details'),
    path('view_doctors', views.view_doctors, name = 'view_doctors'),
    path('doctor_details/<int:doctor_id>/', views.doctor_details, name='doctor_details'),
    path('bookappointment', views.bookappointment, name='bookappointment'),
    path('view_appointments', views.view_appointments, name = 'view_appointments'),
    path('view_nurses', views.view_nurses, name= 'view_nurses'),
    path('nurse_details/<int:nurse_id>/', views.nurse_details, name='nurse_details'),
    path('nurse_details', views.nurse_details, name='nurse_details'),
    path('view_wards', views.view_wards, name='view_wards'),
    path('view_billings', views.view_billings, name='view_billings'),
    path('view_departments/', views.view_departments, name='view_departments'),
    path('view_beds', views.view_beds, name='view_beds'),
    path('view_medications', views.view_medications, name='view_medications'),
    path('view_tests', views.view_tests, name='view_tests'),
    path('view_procedures', views.view_procedures, name= 'view_procedures'),
    path('view_shifts', views.view_shifts, name='view_shifts'),
    path('view_admissions', views.view_admissions, name='view_admissions'),
    path('view_discharges', views.view_discharges, name='view_discharges'),



        #    api views

    path('api/patients/', api_views.get_patients, name='get_patients'),
    path('api/patients/new/', api_views.create_patient, name='create_patient'),
    path('api/patients/<int:id>/', api_views.get_patient, name='get_patient'),
    path('api/patients/<int:id>/delete', api_views.delete_patient, name='delete_patient'),
    path('api/patients/<int:id>/update', api_views.update_patient, name='update_patient'),
    path('api/doctors/', api_views.get_doctors, name='get_doctors'),
    path('api/doctors/new/', api_views.create_doctor, name='create_doctor'),
    path('api/doctors/<int:id>/', api_views.get_doctor, name='get_doctor'),
    path('api/doctors/<int:id>/delete', api_views.delete_doctor, name='delete_doctor'),
    path('api/doctors/<int:id>/update', api_views.update_doctor, name='update_doctor'),
    path('api/appointments/', api_views.get_appointments, name='get_appointments'),
    path('api/appointments/<int:id>/', api_views.get_apppointment, name='get_apppointment'),
    path('api/appointments/new/', api_views.create_appointment, name='create_apppointment'),
    path('api/appointments/<int:id>/delete', api_views.delete_apppointment, name='delete_apppointment'),
    path('api/appointments/<int:id>/update', api_views.update_apppointment, name='update_apppointment'),
    path('api/departments/', api_views.get_departments, name='get_departments'),
    path('api/departments/new/', api_views.create_department, name='create_department'),
    path('api/departments/<int:id>/', api_views.get_department, name='get_department'),
    path('api/departments/<int:id>/delete', api_views.delete_department, name='delete_department'),
    path('api/departments/<int:id>/update', api_views.update_department, name='delete_department'),
    path('api/beds/', api_views.get_beds, name='get_beds'),
    path('api/beds/new/', api_views.create_bed, name='create_bed'),
    path('api/beds/<int:id>/', api_views.get_bed, name='get_bed'),
    path('api/beds/<int:id>/delete', api_views.delete_bed, name='delete_bed'),
    path('api/beds/<int:id>/update', api_views.update_bed, name='update_bed'),
    path('api/medications/', api_views.get_medications, name='get_medications'),
    path('api/medications/new/', api_views.create_medication, name='create_medication'),
    path('api/medications/<int:id>/', api_views.get_medication, name='get_medication'),
    path('api/medications/<int:id>/delete', api_views.delete_medication, name='delete_medication'),
    path('api/medications/<int:id>/update', api_views.update_medication, name='delete_medication'),
    path('api/tests/', api_views.get_tests, name='get_tests'),
    path('api/tests/new/', api_views.create_test, name='create_test'),
    path('api/tests/<int:id>/', api_views.get_test, name='get_test'),
    path('api/tests/<int:id>/delete', api_views.delete_test, name='delete_test'),
    path('api/tests/<int:id>/update', api_views.update_test, name='update_test'),
    path('api/procedures/', api_views.get_procedures, name='get_procedures'),
    path('api/procedures/new/', api_views.create_procedure, name='create_procedure'),
    path('api/procedures/<int:id>/', api_views.get_procedure, name='get_procedure'),
    path('api/procedures/<int:id>/delete', api_views.delete_procedure, name='delete_procedure'),
    path('api/procedures/<int:id>/update', api_views.update_procedure, name='update_procedure'),
    path('api/billings/', api_views.get_billings, name='get_billings'),
    path('api/billings/new/', api_views.create_billing, name='create_billing'),
    path('api/billings/<int:id>/', api_views.get_billing, name='get_billing'),
    path('api/billings/<int:id>/delete', api_views.delete_billing, name='delete_billing'),
    path('api/billings/<int:id>/update', api_views.update_billing, name='delete_billing'),
    path('api/nurses/', api_views.get_nurses, name='get_nurses'),
    path('api/nurses/new/', api_views.create_nurse, name='create_nurse'),
    path('api/nurses/<int:id>/', api_views.get_nurse, name='get_nurse'),
    path('api/nurses/<int:id>/delete', api_views.delete_nurse, name='delete_nurse'),
    path('api/nurses/<int:id>/update', api_views.update_nurse, name='update_nurse'),
    path('api/wards/', api_views.get_wards, name='get_wards'),
    path('api/wards/new/', api_views.create_ward, name='create_ward'),  
    path('api/wards/<int:id>/', api_views.get_ward, name='get_ward'),
    path('api/wards/<int:id>/delete', api_views.delete_ward, name='delete_ward'),
    path('api/wards/<int:id>/update', api_views.update_ward, name='update_ward'),
    path('api/shifts/', api_views.get_shifts, name='get_shifts'),
    path('api/shifts/new/', api_views.create_shift, name='create_shift'),
    path('api/shifts/<int:id>/', api_views.get_shift, name='get_shift'),
    path('api/shifts/<int:id>/delete', api_views.delete_shift, name='delete_shift'),
    path('api/shifts/<int:id>/update', api_views.update_shift, name='update_shift'),
    path('api/admissions/', api_views.get_admissions, name='get_admissions'),
    path('api/admissions/new/', api_views.create_admission, name='create_admission'),
    path('api/admissions/<int:id>/', api_views.get_admission, name='get_admission'),
    path('api/admissions/<int:id>/delete', api_views.delete_admission, name='delete_admission'),
    path('api/admissions/<int:id>/update', api_views.update_admission, name='update_admission'),
    path('api/discharges/', api_views.get_discharges, name='get_discharges'),
    path('api/discharges/new/', api_views.create_discharge, name='create_discharge'),
    path('api/discharges/<int:id>/', api_views.get_discharge, name='get_discharge'),
    path('api/discharges/<int:id>/delete', api_views.delete_discharge, name='delete_discharge'),
    path('api/discharges/<int:id>/update', api_views.update_discharge, name='update_discharge'),
    
     
]
