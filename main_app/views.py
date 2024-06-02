from django.shortcuts import render , redirect
from main_app.forms import LoginForm, PatientForm , DoctorForm , AppointmentForm , NurseForm , WardForm, BillingForm, BedForm, MedicationForm
from django.contrib.auth import authenticate, login
from django.http import JsonResponse
from django.http import HttpResponse
from .models import Appointment, Billing,Bed, Medication

import requests

# Create your views here.



def getwellpage(request):
    return render(request, 'getwell.html')


def signin(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')  
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'home.html')


def view_patients(request):
    api_url = 'http://localhost:8000/api/patients/'
    response = requests.get(api_url)
    if response.status_code == 200:
        patients= response.json()
        return render(request, 'view_patients.html', {'patients': patients})
    else:
        error_message = response.json().get('message', 'Failed to fetch patients.')
        return render(request, 'patient.html', {'error_message': error_message})



def patient_details(request, patient_id):
    api_url = f'http://localhost:8000/api/patients/{patient_id}'

    try:
        response = requests.get(api_url)
        response.raise_for_status() 

        # Parse JSON response
        patient_data = response.json()
        return render(request, 'patient_details.html', {'patient': patient_data})

    except requests.exceptions.RequestException as e:
        # Handle API request errors
        error_message = f'Error fetching patient details: {e}'
        return render(request, 'patient_details.html', {'error': error_message})




def view_doctors(request):
    api_url = 'http://localhost:8000/api/doctors/'
    response = requests.get(api_url)
    if response.status_code == 200:
        doctors = response.json()
        return render(request, 'view_doctors.html', {'doctors': doctors})
    else:
        error_message = response.json().get('message', 'Failed to fetch doctors.')
        return render(request, 'doctor.html', {'error_message': error_message})


def doctor_details(request, doctor_id):
    api_url = f'http://localhost:8000/api/doctors/{doctor_id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        doctor_details = response.json()
        return render(request, 'doctor_details.html', {'doctor_details': doctor_details})
    else:
        error_message = response.json().get('message', 'Failed to fetch doctor details.')
        return render(request, 'view_doctors', {'error_message': error_message})



# def bookappointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             api_url = 'http://localhost:8000/api/appointments/'
#             appointment_data = {
#                 'patient': form.cleaned_data['patient'],
#                 'doctor': form.cleaned_data['doctor'],
#                 'date': form.cleaned_data['date'],
#                 'time':form.cleaned_data['time'],
#                 'reason':form.cleaned_data['reason'],
#             }
#             response = requests.post(api_url, json=appointment_data)
#             if response.status_code == 201:
#                 return redirect('view_appointments')
#             else:
#                 error_message = response.json().get('message', 'Unknown error')
#                 return render(request, 'bookappointment.html', {'form': form, 'error_message': error_message})
    # else:
    #     form = AppointmentForm()
    # return render(request, 'bookappointment.html', {'form': form})

# def bookappointment(request):
#     if request.method == 'POST':
#         form = AppointmentForm(request.POST)
#         if form.is_valid():
#             form.save()
#             return redirect('view_appointments')
#         else:
#             # Display validation errors
#             for field, errors in form.errors.items():
#                 for error in errors:
#                     messages.error(request, f"Error in {field}: {error}")
#     else:
#         form = AppointmentForm()
#     return render(request, 'bookappointment.html', {'form': form})

def bookappointment(request):
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            # Save the appointment to the local database
            form.save()
            # Redirect to the appointments list page
            return redirect('view_appointments')
    else:
        form = AppointmentForm()
    return render(request, 'bookappointment.html', {'form': form})

    

def view_appointments(request):
    api_url = 'http://localhost:8000/api/appointments/'
    response = requests.get(api_url)
    if response.status_code == 200:
        appointments_data = response.json()
        appointments = []
        for appointment_data in appointments_data:
            appointment = Appointment(
                id=appointment_data['id'],
                patient_id=appointment_data['patient'],
                doctor_id=appointment_data['doctor'],
                date=appointment_data['date'],
                time =appointment_data['time'],
                reason=appointment_data['reason'],
                # Add more fields as needed
            )
            appointments.append(appointment)
        return render(request, 'view_appointments.html', {'appointments': appointments})
    else:
        error_message = response.json()['message']
        return render(request, 'view_appointments.html', {'error_message': error_message})





def view_nurses(request):
    api_url = 'http://localhost:8000/api/nurses/'
    response = requests.get(api_url)
    if response.status_code == 200:
        nurses = response.json()
        return render(request, 'view_nurses.html', {'nurses': nurses})
    else:
        error_message = response.json().get('message', 'Failed to fetch nurses.')
        return render(request, 'nurse.html', {'error_message': error_message})


def nurse_details(request, nurse_id):
    api_url = f'http://localhost:8000/api/nurses/{nurse_id}'
    response = requests.get(api_url)
    if response.status_code == 200:
        nurse_details = response.json()
        return render(request, 'nurse_details.html', {'doctor_details': nurse_details})
    else:
        error_message = response.json().get('message', 'Failed to fetch nurse details.')
        return render(request, 'view_nurses', {'error_message': error_message})




    

def view_wards(request):
    api_url = 'http://localhost:8000/api/wards/'
    response = requests.get(api_url)
    if response.status_code == 200:
        wards = response.json()
        return render(request, 'view_wards.html', {'wards': wards})
    else:
        error_message = response.json().get('message', 'Failed to fetch wards.')
        return render(request, 'ward.html', {'error_message': error_message})



# def view_billings(request):
#     api_url = 'http://localhost:8000/api/billings/'
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         billings = response.json()
#         return render(request, 'view_billings.html', {'billings': billings})
#     else:
#         error_message = response.json().get('message', 'Failed to fetch billings.')
#         return render(request, 'view_patients.html', {'error_message': error_message})



def view_billings(request):
    api_url = 'http://localhost:8000/api/billings/'
    response = requests.get(api_url)
    if response.status_code == 200:
        billings = response.json()
        
        # Fetch patients' details to replace IDs with names
        patients_api_url = 'http://localhost:8000/api/patients/'
        patients_response = requests.get(patients_api_url)
        if patients_response.status_code == 200:
            patients_data = patients_response.json()
            patients_mapping = {patient['id']: patient['name'] for patient in patients_data}
            
            # Replace patient IDs with names in billings
            for billing in billings:
                patient_id = billing['patient']
                if patient_id in patients_mapping:
                    billing['patient_name'] = patients_mapping[patient_id]
                else:
                    billing['patient_name'] = f'Unknown Patient ({patient_id})'
            
            return render(request, 'view_billings.html', {'billings': billings})
        else:
            error_message = patients_response.json().get('message', 'Failed to fetch patients.')
            return render(request, 'view_patients.html', {'error_message': error_message})
    else:
        error_message = response.json().get('message', 'Failed to fetch billings.')
        return render(request, 'view_patients.html', {'error_message': error_message})


        

# def view_billings(request):
#     # Retrieve all billing objects from the database
#     billings = Billing.objects.all()

#     # Serialize the billing data
#     billing_data = []
#     for billing in billings:
#         billing_data.append({
#             'id': billing.id,
#             'patient_name': billing.patient.name,
#             'amount': str(billing.amount),
#             'date_time': billing.date_time.strftime('%Y-%m-%d %H:%M:%S'),
#             'payment_method': billing.payment_method
#         })

#     # Return the serialized data as JSON response
#     return JsonResponse({'billings': billing_data})





def view_departments(request):
    api_url = 'http://localhost:8000/api/departments/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        departments = response.json()
        for department in departments:
            # Assuming the head_of_department field is a foreign key to the doctor model
            id = department.get('head_of_department')
            if id:
                # Make API request to fetch doctor details
                doctor_url = f'http://localhost:8000/api/doctors/{id}/'
                doctor_response = requests.get(doctor_url)
                if doctor_response.status_code == 200:
                    doctor_data = doctor_response.json()
                    # Add doctor name and specialization to the department dictionary
                    department['head_of_department_name'] = doctor_data.get('name')
                    department['head_of_department_specialization'] = doctor_data.get('specialization')
                else:
                    # Handle error fetching doctor details
                    department['head_of_department_name'] = 'N/A'
                    department['head_of_department_specialization'] = 'N/A'
            else:
                # No head of department specified
                department['head_of_department_name'] = 'N/A'
                department['head_of_department_specialization'] = 'N/A'
        
        return render(request, 'view_departments.html', {'departments': departments})
    else:
        error_message = response.json().get('message', 'Failed to fetch departments.')
        return render(request, 'error.html', {'error_message': error_message})




# def view_departments(request):
#     api_url = 'http://localhost:8000/api/departments/'
#     response = requests.get(api_url)
#     if response.status_code == 200:
#         departments= response.json()
#         return render(request, 'view_departments.html', {'departments': departments})
#     else:
#         error_message = response.json().get('message', 'Failed to fetch departments.')
#         return render(request, 'view_doctors.html', {'error_message': error_message})



def view_beds(request):
    api_url = 'http://localhost:8000/api/beds/'
    response = requests.get(api_url)
    if response.status_code == 200:
        beds_data = response.json()
        beds = []
        for bed_data in beds_data:
            bed= Bed(
                id= bed_data['id'],
                department_id=bed_data['department'],
                patient_id=bed_data['patient'],
                number=bed_data['number'],
                is_occupied =bed_data['is_occupied'],
                bed_type=bed_data['bed_type'],
                ward_id = bed_data['ward']
                # Add more fields as needed
            )
            beds.append(bed)
        return render(request, 'view_beds.html', {'beds': beds})
    else:
        error_message = response.json()['message']
        return render(request, 'view_patients.html', {'error_message': error_message})





def view_medications(request):
    api_url = 'http://localhost:8000/api/medications/'
    response = requests.get(api_url)
    
    if response.status_code == 200:
        medications_data = response.json()

        medication_ids = [med['id'] for med in medications_data]
        medications = Medication.objects.filter(id__in=medication_ids).select_related('prescribing_doctor')
        

        return render(request, 'view_medications.html', {'medications': medications})
    else:
        error_message = response.json().get('message', 'Failed to fetch medications.')
        return render(request, 'view_doctors.html', {'error_message': error_message})





def view_tests(request):
    api_url = 'http://localhost:8000/api/tests/'
    response = requests.get(api_url)
    if response.status_code == 200:
        tests = response.json()
        return render(request, 'view_tests.html', {'tests': tests})
    else:
        error_message = response.json().get('message', 'Failed to fetch tests.')
        return render(request, 'view_doctors.html', {'error_message': error_message})


def view_procedures(request):
    api_url = 'http://localhost:8000/api/procedures/'
    respond = requests.get(api_url)
    if respond.status_code ==200:
        procedures = respond.json()
        return render (request, 'view_procedures.html',{'procedures':procedures})
    else:
        error_message = respond.json().get('message', 'Failed to fetch the procedures.')
        return render (request, 'view_doctors.html',{'error_message':error_message})




def view_shifts(request):
    api_url = 'http://localhost:8000/api/shifts/'
    respond = requests.get(api_url)
    if respond.status_code == 200:
        shifts = respond.json()
        return render (request, 'view_shifts.html',{'shifts':shifts})
    else:
        error_message = respond.json().get('message', 'Failed to fetch the shifts')
        return render (request, 'view_shifts.html',{'error_message':error_message})


def view_admissions(request):
    api_url = 'http://localhost:8000/api/admissions/'
    respond = requests.get(api_url)
    if respond.status_code ==200:
        admissions = respond.json()
        return render (request, 'view_admissions.html',{'admissions':admissions})
    else:
        error_message = respond.json().get('message', 'Failed to fetch the procedures.')
        return render (request, 'view_doctors.html',{'error_message':error_message})



def view_discharges(request):
    api_url = 'http://localhost:8000/api/discharges/'
    respond = requests.get(api_url)
    if respond.status_code== 200:
        discharges = respond.json()
        return render(request, 'view_discharges.html',{'discharges':discharges})
    else:
        error_message = request.json().get('message',"Failed to fetch the discharges")
        return render (request, 'view_doctors.html', {'error_message':error_message})



