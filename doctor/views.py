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


class HealthSys(object):
    def dispatch(self, request, *args, **kwargs):
        appointment_id = request.session.get("appointment_id")
        if appointment_id:
            appointment_obj = Appointment.objects.get(id=appointment_id)
            if request.user.is_authenticated and request.user.patient:
                appointment_obj.patient = request.user.patient
                appointment_obj.save()
        return super().dispatch(request, *args, **kwargs)


class ConsultantView(HealthSys,TemplateView):
    template_name = "consultant.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['alldepartment'] = Department.objects.all()
        return context

class ConsultantDetailView(HealthSys,TemplateView):
    template_name = "consultantdetails.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        url_slug = self.kwargs['slug']
        consultant = Consultant.objects.get(slug=url_slug)
        consultant.save()
        context['consultant'] = consultant
        return context



# Create your views here.
