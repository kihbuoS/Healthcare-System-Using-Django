from django import forms
from .models import Department,Consultant
from django.contrib.auth.models import User
class DepartmentForm(forms.ModelForm):
    class Meta:
        model  = Department
        fields = "__all__"
class ConsultantForm(forms.ModelForm):
    class Meta:
        model = Consultant
        fields = "__all__"