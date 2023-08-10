from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import AppointmentForm
from doctor.models import Consultant

def appointmentview(request):
    form = AppointmentForm()
    if request.method == 'POST':
        form = AppointmentForm(request.POST)
        if form.is_valid():
            form.save()

        return redirect("home")

    return render(request,"appointment.html",{'form':form})

    
#AJAX
def load_consultant(request):
    department_id = request.GET.get('department_id')
    consults = Consultant.objects.filter(department_id=department_id).all()
    return render(request,'consultname.html',{'consults':consults})