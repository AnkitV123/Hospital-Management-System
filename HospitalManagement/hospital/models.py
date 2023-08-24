from django.db import models


class Doctor(models.Model):
    name = models.CharField(max_length=50)
    d_dob = models.DateField()
    d_email = models.CharField(max_length=100)
    mobile = models.CharField(max_length=10)
    d_aadhar = models.CharField(max_length=12)
    specialization = models.CharField(max_length=50)
    qualification = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Patient(models.Model):
    registrationDate = models.DateField()
    name = models.CharField(max_length=50)
    gender = models.CharField(max_length=10)
    p_dob = models.DateField()
    mobile = models.CharField(max_length=10, null=True)
    p_email = models.CharField(max_length=100)
    address = models.CharField(max_length=150)
    p_aadhar = models.CharField(max_length=12)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    bloodgroup = models.CharField(max_length=3)
    disease = models.CharField(max_length=50)

    def __str__(self):
        return self.name


class Appointment(models.Model):
    doctor = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date1 = models.DateField(null=True)
    time1 = models.TimeField(max_length=150)

    def __str__(self):
        return self.doctor.name+"--"+self.patient.name


class Prescription(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    med = models.CharField(max_length=150)
    dnd = models.CharField(max_length=150)

    def __str__(self):
        return self.patient.name

# Create your models here.
