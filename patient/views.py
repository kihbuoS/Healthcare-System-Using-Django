from http.client import HTTPResponse
from django.views.generic import View, TemplateView, CreateView, FormView, DetailView, ListView
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.urls import reverse_lazy, reverse
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.http import JsonResponse
from django.conf import settings
from django.db.models import Q
from patient.models import *
from patient.forms import *
from appointment.models import *
from doctor.models import *
from appointment.forms import *
from doctor.forms import *
import requests


# class HealthSys(object):
#     def dispatch(self, request, *args, **kwargs):
#         appointment_id = request.session.get("appointment_id")
#         if appointment_id:
#             appointment_obj = Appointment.objects.get(id=appointment_id)
#             if request.user.is_authenticated and request.user.patient:
#                 appointment_obj.patient = request.user.patient
#                 appointment_obj.save()
#         return super().dispatch(request, *args, **kwargs)

# home
def home(request):
    return render(request,"home.html")

# user registration
class PatientRegistrationView(CreateView):
    template_name = "patientregistration.html"
    form_class = PatientRegistrationForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        username = form.cleaned_data.get("username")
        password = form.cleaned_data.get("password")
        email = form.cleaned_data.get("email")
        user = User.objects.create_user(username, email, password)
        form.instance.user = user
        user.save()
        login(self.request, user)
        return super().form_valid(form)

    # def get_success_url(self):
    #     if "next" in self.request.GET:
    #         next_url = self.request.GET.get("next")
    #         return next_url
    #     else:
    #         return self.success_url
# user login view
class PatientLoginView(FormView):
    template_name = "patientlogin.html"
    form_class = PatientLoginForm
    success_url = reverse_lazy("home")

    def form_valid(self, form):
        uname = form.cleaned_data.get("username")
        pword = form.cleaned_data["password"]
        usr = authenticate(username=uname, password=pword)
        if usr is not None and Patient.objects.filter(user=usr).exists():
            login(self.request, usr)
        else:
            return render(self.request, self.template_name, {"form": self.form_class, "error": "Invalid credentials"})

        return super().form_valid(form)

    # def get_success_url(self):
    #     if "next" in self.request.GET:
    #         next_url = self.request.GET.get("next")
    #         return next_url
    #     else:
    #         return self.success_url

# patient Profile

class PatientProfileView(TemplateView):
    template_name = "patientprofile.html"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Patient.objects.filter(user=request.user).exists():
            pass
        else:
            return HTTPResponse("sorry you don't have id")
            # return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        patient = self.request.user.patient
        context['patient'] = patient
        appointments = Appointment.objects.filter(appointment__patient=patient).order_by("-id")
        context["appointments"] = appointments
        return context

#Appointment Details 

class AppointmentDetailView(DetailView):
    template_name = "Appointmentdetail.html"
    model = Appointment
    context_object_name = "ord_obj"

    def dispatch(self, request, *args, **kwargs):
        if request.user.is_authenticated and Patient.objects.filter(user=request.user).exists():
            appointment_id = self.kwargs["pk"]
            appointment = Appointment.objects.get(id=appointment_id)
            if request.user.patient != appointment.patient:
                return redirect("ecomapp:customerprofile")
        else:
            return redirect("/login/?next=/profile/")
        return super().dispatch(request, *args, **kwargs)

# logout
class signoutview(View):
    def get(self,request):
        logout(request)
        return redirect("home")



