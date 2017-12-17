from django.db import models
from django.utils import timezone

class Doctor(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    specialization = models.CharField(max_length=20)
    class Meta:
        app_label = 'app'

class MedicalExamination(models.Model):
    name = models.CharField(max_length=25)
    start_time = models.DateTimeField()
    duration = models.TimeField()
    result = models.TextField()
    was_performed = models.BooleanField()
    additional_info = models.TextField()
    class Meta:
        app_label = 'app'

class Patient(models.Model):
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    personal_id = models.CharField(max_length=20)
    birth_date = models.DateTimeField()
    additional_info = models.TextField()
    class Meta:
        app_label = 'app'

class Room(models.Model):
    additional_info = models.TextField()
    class Meta:
        app_label = 'app'

class Task(models.Model):
    doctor_id = models.ForeignKey(Doctor)
    patient_id = models.ForeignKey(Patient)
    medical_examination_id = models.ForeignKey(MedicalExamination)
    room_id = models.ForeignKey(Room)
    additional_info = models.TextField()
    class Meta:
        app_label = 'app'

    

    
