from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('',ConsultantView.as_view(),name="consultant"),
    path("consultantdetails",ConsultantDetailView.as_view(),name="consultantdetails")

]
