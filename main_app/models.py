from django.db import models




# Create your models here.

# models.py
class Patient(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField()
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
    ]
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()
    medical_history = models.TextField()
    insurance_details = models.TextField()
    # bed= models.ForeignKey('Bed', on_delete=models.CASCADE, related_name='patients',default=None, null=True)
    
   
    def __str__(self):
        return self.name


class Doctor(models.Model):
    name = models.CharField(max_length=100)
    specialization = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    qualifications = models.TextField()
    schedule = models.CharField(max_length=100)

    def __str__(self):
        return self.name

        

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()

    def __str__(self):
        return f"Appointment for {self.patient.name} with Dr. {self.doctor.name} on {self.date} at {self.time}"



class Department(models.Model):
    name = models.CharField(max_length=100)
    head_of_department = models.ForeignKey(Doctor, on_delete=models.SET_NULL, null=True)
    description = models.TextField()

    def __str__(self):
        return self.name




class Bed(models.Model):
    department = models.ForeignKey(Department, on_delete=models.CASCADE, default=False)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)
    number = models.CharField(max_length=10)
    is_occupied = models.BooleanField(default=False)
    bed_type = models.CharField(max_length=50)
    ward = models.ForeignKey('Ward', on_delete=models.CASCADE, default=None,)

    def __str__(self):
        return f"Bed {self.number} in {self.department.name} with {self.patient.name}"





class Medication(models.Model):
    name = models.CharField(max_length=100)
    dosage = models.CharField(max_length=50)
    administration_route = models.CharField(max_length=50)
    prescribing_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    frequency = models.CharField(max_length=50)

    def __str__(self):
        return self.name




class Test(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE, default=None)
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    ordering_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    result = models.TextField()

    def __str__(self):
        return self.name




class Procedure(models.Model):
    name = models.CharField(max_length=100)
    date_time = models.DateTimeField()
    performing_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    outcome = models.TextField()

    def __str__(self):
        return self.name



class Billing(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date_time = models.DateTimeField()
    payment_method = models.CharField(max_length=50)

    def __str__(self):
        return f"Billing for {self.patient.name} - ${self.amount}"



class Nurse(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    contact_number = models.CharField(max_length=15)
    address = models.TextField()

    def __str__(self):
        return self.name



class Ward(models.Model):
    name = models.CharField(max_length=100)
    capacity = models.IntegerField()
    current_occupancy = models.IntegerField()

    def __str__(self):
        return self.name




class Shift(models.Model):
    nurse = models.ForeignKey(Nurse, on_delete=models.CASCADE)
    start_time = models.TimeField()
    end_time = models.TimeField()
    department = models.ForeignKey(Department, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.nurse.name}'s shift in {self.department.name}"



class Admission(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    admission_date_time = models.DateTimeField()
    admitting_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f"Admission of {self.patient.name} at {self.admission_date_time}"



class Discharge(models.Model):
    admission = models.OneToOneField(Admission, on_delete=models.CASCADE)
    discharge_date_time = models.DateTimeField()
    discharging_doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    reason = models.TextField()

    def __str__(self):
        return f"Discharge of {self.admission.patient.name} at {self.discharge_date_time}"
