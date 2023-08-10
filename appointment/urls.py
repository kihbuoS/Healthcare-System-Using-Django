from django.urls import path
from . import views

urlpatterns = [
    path('',views.appointmentview,name="appointment"),
    path('ajax/load-consultant/',views.load_consultant,name="ajax_load_consultant"),#AJAX
]
