
from django.db import models
from patient.models import Patient
from doctor.models import Department,Consultant
import uuid

TYPE = (
    ("Physical Visit", "Physical Visit"),
    ("Teleconsultation","Teleconsultation")
)

Time = (
    ("09.30 AM - 10.00 AM", "09.30 AM - 10.00 AM"),
    ("10.00 AM - 10.30 AM", "10.00 AM - 10.30 AM"),
    ("10.30 AM - 11.00 AM", "10.30 AM - 11.00 AM"),
    ("11.00 AM - 11.30 AM", "11.00 AM - 11.30 AM"),
    ("11.30 AM - 12.00 PM", "11.30 AM - 12.00 PM"),
    ("12.00 PM - 12.30 PM", "12.00 PM - 12.30 PM"),
    ("12.30 PM - 01.00 PM", "12.30 PM - 01.00 PM"),
)

class Appointment(models.Model):
    uid = models.UUIDField(primary_key=True,editable=False,default=uuid.uuid4)
    patient = models.ForeignKey(Patient, on_delete=models.SET_NULL, null=True, blank=True,editable=False)
    name = models.CharField(max_length=200)
    email = models.EmailField(null=True,blank=True)
    mobile =models.CharField(max_length=10)
    department = models.ForeignKey(Department, on_delete=models.SET_NULL, null=True, blank=True)
    consultant = models.ForeignKey(Consultant, on_delete=models.SET_NULL, null=True, blank=True)
    date = models.DateTimeField(auto_now_add=True)
    timeslot = models.CharField(max_length=100,choices=Time,default="Select Time Slot")
    consultant_type = models.CharField(max_length=100,choices=TYPE,default="Select Type")
    message = models.TextField()

    def __str__(self):
        return "uuid number"+ str(self.uid)+"patient name"+ str(self.name)

