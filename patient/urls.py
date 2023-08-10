from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('signup',PatientRegistrationView.as_view(),name="signup"),
    path('signin',PatientLoginView.as_view(),name="signin"),
    path('signout',signoutview.as_view,name='signout'),
    path('patientprofile',PatientProfileView.as_view(),name="patientprofile"),
    path('',views.home,name="home"),
    path('appointmentdetails',AppointmentDetailView.as_view(),name="appointmentdetails")
]
