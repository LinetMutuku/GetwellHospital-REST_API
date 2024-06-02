from rest_framework import serializers
from main_app.models import Patient , Doctor, Appointment, Department, Bed , Medication, Test, Procedure, Billing , Nurse, Ward ,Shift , Admission, Discharge



class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model= Patient
        fields = "__all__"



class DoctorSerializer(serializers.ModelSerializer):
    class Meta:
        model= Doctor
        fields = "__all__"


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Appointment
        fields = "__all__"


class DepartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model= Department
        fields = "__all__"


class BedSerializer(serializers.ModelSerializer):
    number = serializers.CharField(required=True)
    bed_type = serializers.CharField(required=True)
    department = serializers.CharField(required=True)
    class Meta:
        model= Bed
        fields = "__all__"



class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model=  Medication
        fields = "__all__"


class TestSerializer(serializers.ModelSerializer):
    class Meta:
        model= Test
        fields = "__all__"



class ProcedureSerializer(serializers.ModelSerializer):
    class Meta:
        model= Procedure
        fields = "__all__"


class BillingSerializer(serializers.ModelSerializer):
    class Meta:
        model= Billing
        fields = "__all__"


class NurseSerializer(serializers.ModelSerializer):
    class Meta:
        model= Nurse
        fields = "__all__"



class WardSerializer(serializers.ModelSerializer):
    class Meta:
        model= Ward
        fields = "__all__"

class ShiftSerializer(serializers.ModelSerializer):
    class Meta:
        model= Shift
        fields = "__all__"


class AdmissionSerializer(serializers.ModelSerializer):
    class Meta:
        model= Admission
        fields = "__all__"


class DischargeSerializer(serializers.ModelSerializer):
    class Meta:
        model= Discharge
        fields = "__all__"