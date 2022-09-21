from django.urls import path, include, re_path
from . import views

urlpatterns = [
    path('login', views.login, name='login'),
    path('administracion', views.administracion, name='admin'),
]


