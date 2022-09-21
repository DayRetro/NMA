from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

#@login_required si se pone esto entonces redirecciona al login si no estas logueado
def inicio(request):
    return render(request, 'inicio.html')


