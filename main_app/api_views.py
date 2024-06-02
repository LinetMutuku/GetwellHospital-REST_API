from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404

from .models import Patient, Doctor, Appointment, Department, Bed , Medication, Test, Procedure, Billing, Nurse, Ward, Shift, Admission, Discharge
from .serializers import PatientSerializer, DoctorSerializer, AppointmentSerializer, DepartmentSerializer, BedSerializer,MedicationSerializer, TestSerializer , ProcedureSerializer, BillingSerializer, NurseSerializer, WardSerializer, ShiftSerializer,AdmissionSerializer, DischargeSerializer


@api_view(['GET'])
def get_patients(request):
    patients = Patient.objects.all()
    serializer = PatientSerializer(instance=patients, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_patient(request):
    serializer = PatientSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Patient saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving patient', 'error': str(e)}, status=400)
  


@api_view(['GET'])
def get_patient(request, id):
    try:
        patient = Patient.objects.get(pk=id)
        serializer = PatientSerializer(instance=patient)
        return Response(serializer.data)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=404)



@api_view(['DELETE'])
def delete_patient(request, id):
        try:
           patient = Patient.objects.get(pk=id)
           patient.delete()
           return Response({'message': 'Patient successfully deleted'})
        except:
             return Response({'error': 'Patient not found'}, status=404)




@api_view(['PUT', 'PATCH'])
def update_patient(request, id):
    try:
        patient = Patient.objects.get(pk=id)
    except Patient.DoesNotExist:
        return Response({'error': 'Patient not found'}, status=404)

    serializer = PatientSerializer(instance=patient, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Patient information updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)




@api_view(['GET'])
def get_doctors(request):
    doctors = Doctor.objects.all()
    serializer = DoctorSerializer(instance=doctors, many=True)
    return Response(serializer.data)



@api_view(['POST'])
def create_doctor(request):
    serializer = DoctorSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Doctor saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Doctor', 'error': str(e)}, status=400)
  
        


@api_view(['GET'])
def get_doctor(request, id):
    try:
        doctor = Doctor.objects.get(pk=id)
        serializer = DoctorSerializer(doctor)
        return Response(serializer.data)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=404)


@api_view(['DELETE'])
def delete_doctor(request, id):
        try:
           doctor = Doctor.objects.get(pk=id)
           doctor.delete()
           return Response({'message': 'Doctor successfully deleted'})
        except:
             return Response({'error': 'Doctor not found'}, status=404)


@api_view(['PUT', 'PATCH'])
def update_doctor(request, id):
    try:
        doctor= Doctor.objects.get(pk=id)
    except Doctor.DoesNotExist:
        return Response({'error': 'Doctor not found'}, status=404)

    serializer = DoctorSerializer(instance=doctor, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Doctor information updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)
  


  
@api_view(['GET'])
def get_appointments(request):
    if request.method == 'GET':
        appointments = Appointment.objects.all()
        serializer = AppointmentSerializer(appointments, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def create_appointment(request):
    serializer = AppointmentSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Appointment saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Appointment', 'error': str(e)}, status=400)
  

@api_view(['GET'])
def get_apppointment(request,id):
    try:
        appointment = Appointment.objects.get(pk=id)
        serializer = AppointmentSerializer(appointment)
        return Response(serializer.data)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=404)



@api_view(['DELETE'])
def delete_apppointment(request, id):
        try:
           appointment = Appointment.objects.get(pk=id)
           appointment.delete()
           return Response({'message': 'Appointment successfully deleted'})
        except:
             return Response({'error': 'Appointment not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_apppointment(request, id):
    try:
        appointment= Appointment.objects.get(pk=id)
    except Appointment.DoesNotExist:
        return Response({'error': 'Appointment not found'}, status=404)

    serializer = AppointmentSerializer(instance=appointment, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Appointment information updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)
  



@api_view(['GET'])
def get_departments(request):
    if request.method == 'GET':
        departments = Department.objects.all()
        serializer = DepartmentSerializer(departments, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_department(request):
    serializer = DepartmentSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Department saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Department', 'error': str(e)}, status=400)
  


@api_view(['GET'])
def get_department(request, id):
    try:
        department= Department.objects.get(pk=id)
        serializer = DepartmentSerializer(instance=department)
        return Response(serializer.data)
    except Patient.DoesNotExist:
        return Response({'error': 'department not found'}, status=404)


@api_view(['DELETE'])
def delete_department(request, id):
    try:
           department = Department.objects.get(pk=id)
           department.delete()
           return Response({'message': 'Department  successfully deleted'})
    except:
             return Response({'error': 'Department not found'}, status=404)




@api_view(['PUT', 'PATCH'])
def update_department(request, id):
    try:
        department= Department.objects.get(pk=id)
    except Department.DoesNotExist:
        return Response({'error': 'Department not found'}, status=404)

    serializer = DepartmentSerializer(instance=department, data=request.data)
    if serializer.is_valid():
        department= serializer.save()
        doctor_name = department.head_of_department.name
        return Response({'message': f'Department information with  H.O.D {doctor_name} updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)




@api_view(['GET'])
def get_beds(request):
    if request.method == 'GET':
        beds = Bed.objects.all()
        serializer = BedSerializer(beds, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def create_bed(request):
    serializer = BedSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Bed saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Bed', 'error': str(e)}, status=400)

# @api_view(['POST'])          
# def create_bed(request):
#     try:
#         bed_id = request.data.get('bed_id')
#         department_id = request.data.get('department_id')
#         bed_name = request.data.get('bed_name')
#         if not department_id:
#             return Response({"message": "Department ID is required"}, status=status.HTTP_400_BAD_REQUEST)
#         try:
#             department = get_object_or_404(Department, id=department_id)
#         except Department.DoesNotExist:
#             return Response({"message": "Invalid Department ID"}, status=status.HTTP_400_BAD_REQUEST)
        
#         if bed_id:
#             bed = get_object_or_404(Bed, id=bed_id)
#             bed.department = department
#             bed.name = bed_name
#         else:
#             bed = Bed(
#                 department=department,
#                 name=bed_name,
                
#             )
#         bed.save()
        
#         return Response({"message": "Bed saved successfully!"}, status=status.HTTP_200_OK)
#     except Exception as e:
#         return Response({"message": "Error saving Bed", "error": str(e)}, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def get_bed(request, id):
    try:
        bed= Bed.objects.get(pk=id)
        serializer = BedSerializer(instance=bed)
        return Response(serializer.data)
    except Bed.DoesNotExist:
        return Response({'error': 'Bed not found'}, status=404)



@api_view(['DELETE'])
def delete_bed(request, id):
    try:
           bed = Bed.objects.get(pk=id)
           bed.delete()
           return Response({'message': 'Bed  successfully deleted'})
    except:
             return Response({'error': 'Bed not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_bed(request, id):
    try:
        bed= Bed.objects.get(pk=id)
    except Bed.DoesNotExist:
        return Response({'error': 'Bed not found'}, status=404)

    serializer = BedSerializer(instance=bed, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Bed information  updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)
   



@api_view(['GET'])
def get_medications(request):
    if request.method == 'GET':
        medications = Medication.objects.all()
        serializer = MedicationSerializer(medications, many=True)
        return Response(serializer.data)




@api_view(['POST'])
def create_medication(request):
    serializer = MedicationSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Medication saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Medication', 'error': str(e)}, status=400)
  


@api_view(['GET'])
def get_medication(request, id):
    try:
        medication= Medication.objects.get(pk=id)
        serializer = MedicationSerializer(instance=medication)
        return Response(serializer.data)
    except Medication.DoesNotExist:
        return Response({'error': 'Medication not found'}, status=404)


@api_view(['DELETE'])
def delete_medication(request, id):
    try:
           medication= Medication.objects.get(pk=id)
           medication.delete()
           return Response({'message': 'Medication  successfully deleted'})
    except:
             return Response({'error': 'Medication not found'}, status=404)


@api_view(['PUT', 'PATCH'])
def update_medication(request, id):
    try:
        medication= Medication.objects.get(pk=id)
    except Medication.DoesNotExist:
         return Response({'error': 'Medication not found'}, status=404)

    serializer = MedicationSerializer(instance=medication, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Medication information  updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)
   

@api_view(['GET'])
def get_tests(request):
    if request.method == 'GET':
        tests = Test.objects.all()
        serializer = TestSerializer(tests, many=True)
        return Response(serializer.data)




@api_view(['POST'])
def create_test(request):
    serializer = TestSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Test saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Test', 'error': str(e)}, status=400)
  




@api_view(['GET'])
def get_test(request, id):
    try:
        test= Test.objects.get(pk=id)
        serializer = TestSerializer(instance=test)
        return Response(serializer.data)
    except Test.DoesNotExist:
        return Response({'error': 'Test not found'}, status=404)


@api_view(['DELETE'])
def delete_test(request, id):
    try:
        test= Test.objects.get(pk=id)
        test.delete()
        return Response({'message': 'Test  successfully deleted'})
    except:
             return Response({'error': 'Test not found'}, status=404)


@api_view(['PUT', 'PATCH'])
def update_test(request, id):
    try:
        test= Test.objects.get(pk=id)
    except Test.DoesNotExist:
         return Response({'error': 'Test not found'}, status=404)

    serializer = TestSerializer(instance=test, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Test information  updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)




@api_view(['GET'])
def get_procedures(request):
    if request.method == 'GET':
        procedures = Procedure.objects.all()  
        serializer = ProcedureSerializer(procedures, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def create_procedure(request):
    serializer = ProcedureSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Procedure  saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving procedure', 'error': str(e)}, status=400)







@api_view(['GET'])
def get_procedure(request, id):
     try:
        procedure= Procedure.objects.get(pk=id)
        serializer = ProcedureSerializer(instance=procedure)
        return Response(serializer.data)
     except Procedure.DoesNotExist:
        return Response({'error': 'Procedure not found'}, status=404)


@api_view(['DELETE'])
def delete_procedure(request, id):
    try:
        procedure= Procedure.objects.get(pk=id)
        procedure.delete()
        return Response({'message': 'Procedure  successfully deleted'})
    except:
             return Response({'error': 'Procedure not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_procedure(request, id):
    try:
        procedure= Procedure.objects.get(pk=id)
    except Procedure.DoesNotExist:
         return Response({'error': 'Procedure not found'}, status=404)

    serializer = ProcedureSerializer(instance=procedure, data=request.data)
    if serializer.is_valid():
        procedure = serializer.save()
        doctor_name = procedure.performing_doctor.name
        return Response({'message': f'Procedure performed by Dr {doctor_name}  updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)



@api_view(['GET'])
def get_billings(request):
     if request.method == 'GET':
        billings= Billing.objects.all()
        serializer = BillingSerializer(billings, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_billing(request):
    serializer = BillingSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Billing saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Billing', 'error': str(e)}, status=400)
  


@api_view(['GET'])
def get_billing(request, id):
    try:
        billing= Billing.objects.get(pk=id)
        serializer = BillingSerializer(instance=billing)
        return Response(serializer.data)
    except Billing.DoesNotExist:
        return Response({'error': 'Billing not found'}, status=404)



@api_view(['DELETE'])
def delete_billing(request, id):
    try:
        billing= Billing.objects.get(pk=id)
        billing.delete()
        return Response({'message': 'The Billing  successfully deleted'})
    except:
             return Response({'error': 'Billing not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_billing(request, id):
    try:
        billing= Billing.objects.get(pk=id)
    except Billing.DoesNotExist:
         return Response({'error': 'Billing not found'}, status=404)

    serializer = BillingSerializer(instance=billing, data=request.data)
    if serializer.is_valid():
        billing = serializer.save()
        patient_name = billing.patient.name
        return Response({'message': f'Billing of  {patient_name}  updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)




@api_view(['GET'])
def get_nurses(request):
     if request.method == 'GET':
        nurses= Nurse.objects.all()
        serializer = NurseSerializer(nurses, many=True)
        return Response(serializer.data)


@api_view(['POST'])
def create_nurse(request):
    serializer = NurseSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Nurse saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Nurse', 'error': str(e)}, status=400)
  


@api_view(['GET'])
def get_nurse(request, id):
    try:
        nurse= Nurse.objects.get(pk=id)
        serializer = NurseSerializer(instance=nurse)
        return Response(serializer.data)
    except Nurse.DoesNotExist:
        return Response({'error': 'Nurse not found'}, status=404)



@api_view(['DELETE'])
def delete_nurse(request, id):
    try:
        nurse= Nurse.objects.get(pk=id)
        nurse.delete()
        return Response({'message': 'Nurse  successfully deleted'})
    except:
             return Response({'error': 'Nurse not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_nurse(request, id):
    try:
        nurse= Nurse.objects.get(pk=id)
    except Nurse.DoesNotExist:
         return Response({'error': 'Nurse not found'}, status=404)

    serializer = NurseSerializer(instance=nurse, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Nurse information updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)




@api_view(['GET'])
def get_wards(request):
     if request.method == 'GET':
        wards= Ward.objects.all()
        serializer = WardSerializer(wards, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def create_ward(request):
    serializer = WardSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Ward saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Ward', 'error': str(e)}, status=400)
  

@api_view(['GET'])
def get_ward(request, id):
     try:
        ward= Ward.objects.get(pk=id)
        serializer = WardSerializer(instance=ward)
        return Response(serializer.data)
     except Ward.DoesNotExist:
        return Response({'error': 'Ward not found'}, status=404)


@api_view(['DELETE'])
def delete_ward(request, id):
    try:
        ward= Ward.objects.get(pk=id)
        ward.delete()
        return Response({'message': 'Ward  successfully deleted'})
    except:
            return Response({'error': 'Ward not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_ward(request, id):
    try:
        ward= Ward.objects.get(pk=id)
    except Ward.DoesNotExist:
         return Response({'error': 'Ward not found'}, status=404)

    serializer = WardSerializer(instance=ward, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Ward information updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)



@api_view(['GET'])
def get_shifts(request):
     if request.method == 'GET':
        shifts= Shift.objects.all()
        serializer = ShiftSerializer(shifts, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def create_shift(request):
    serializer = ShiftSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Shift saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Shift', 'error': str(e)}, status=400)
  



@api_view(['GET'])
def get_shift(request, id):
     try:
        shift= Shift.objects.get(pk=id)
        serializer = ShiftSerializer(instance=shift)
        return Response(serializer.data)
     except Shift.DoesNotExist:
        return Response({'error': 'Shift not found'}, status=404)



@api_view(['DELETE'])
def delete_shift(request, id):
    try:
        shift= Shift.objects.get(pk=id)
        shift.delete()
        return Response({'message': 'Shift  successfully deleted'})
    except:
           return Response({'error': 'Shift not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_shift(request, id):
    try:
        shift= Shift.objects.get(pk=id)
    except Shift.DoesNotExist:
         return Response({'error': 'Shift not found'}, status=404)

    serializer = ShiftSerializer(instance=shift, data=request.data)
    if serializer.is_valid():
        shift = serializer.save()
        nurse_name = shift.nurse.name
        department_name = shift.department.name
        return Response({'message': f'Shift with {nurse_name}  in department {department_name} information updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)



@api_view(['GET'])
def get_admissions(request):
     if request.method == 'GET':
        admissions= Admission.objects.all()
        serializer = AdmissionSerializer(admissions, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def create_admission(request):
    serializer = AdmissionSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Admission saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Admission', 'error': str(e)}, status=400)
  


@api_view(['GET'])
def get_admission(request, id):
     try:
        admission= Admission.objects.get(pk=id)
        serializer = AdmissionSerializer(instance=admission)
        return Response(serializer.data)
     except Admision.DoesNotExist:
        return Response({'error': 'Admission not found'}, status=404)



@api_view(['DELETE'])
def delete_admission(request, id):
    try:
        admission= Admission.objects.get(pk=id)
        admission.delete()
        return Response({'message': 'Admission  successfully deleted'})
    except:
           return Response({'error': 'Admission not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_admission(request, id):
    try:
        admission= Admission.objects.get(pk=id)
    except Admission.DoesNotExist:
         return Response({'error': 'Admission not found'}, status=404)

    serializer = AdmissionSerializer(instance=admission, data=request.data)
    if serializer.is_valid():
        admission = serializer.save()
        patient_name = admission.patient.name
        doctor_name = admission.admitting_doctor.name
        return Response({'message': f'Admission of {patient_name} admitted by {doctor_name} information updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)



@api_view(['GET'])
def get_discharges(request):
    if request.method == 'GET':
        discharges= Discharge.objects.all()
        serializer = DischargeSerializer(discharges, many=True)
        return Response(serializer.data)



@api_view(['POST'])
def create_discharge(request):
    serializer = DischargeSerializer(data=request.data)
    try:
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({'message': 'Discharge saved successfully', 'data': serializer.data}, status=201)
    except Exception as e:
        return Response({'message': 'Error saving Discharge', 'error': str(e)}, status=400)
  


@api_view(['GET'])
def get_discharge(request, id):
     try:
        discharge= Discharge.objects.get(pk=id)
        serializer = DischargeSerializer(instance=discharge)
        return Response(serializer.data)
     except Discharge.DoesNotExist:
        return Response({'error': 'Discharge not found'}, status=404)



@api_view(['DELETE'])
def delete_discharge(request, id):
    try:
        discharge = Discharge.objects.get(pk=id)
        discharge.delete()
        return Response({'message': 'Discharge  successfully deleted'})
    except:
           return Response({'error': 'Discharge not found'}, status=404)



@api_view(['PUT', 'PATCH'])
def update_discharge(request, id):
    try:
        discharge= Discharge.objects.get(pk=id)
    except Discharge.DoesNotExist:
         return Response({'error': 'Discharge not found'}, status=404)

    serializer = DischargeSerializer(instance=discharge, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'message': 'Discharge information updated successfully', 'data': serializer.data})
    return Response(serializer.errors, status=400)













    
































        

























