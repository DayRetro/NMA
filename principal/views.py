import imp
from django.shortcuts import render
from django.http import HttpRequest

# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def login(request):
    return render(request, 'login.html')
