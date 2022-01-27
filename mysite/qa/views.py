from django.shortcuts import render
from django.template import context
from .models import *
from django.shortcuts import render

def home(request):
    questions=Question.objects.all()
    context = {
       'questions':questions 
    }
    return render(request,'qa/home.html',context)