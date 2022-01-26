from django.shortcuts import render
from django.template import context
from .models import *
from django.views.generic import ListView, CreateView


def home(request):
    return render(request,'qa/home.html')