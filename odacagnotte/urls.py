from .views import *
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Motif.as_view()),
]

