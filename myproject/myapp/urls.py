from django.urls import path
from . import views

urlpatterns = [
    path('getform/', views.getform),
    path('clguess/', views.GuessGameViev.as_view())
]
