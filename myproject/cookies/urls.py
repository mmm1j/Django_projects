from django.urls import path
from . import views

urlpatterns = [
    path('cookies/', views.cookies),
]
