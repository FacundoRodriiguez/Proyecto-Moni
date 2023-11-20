
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
import requests
from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login

# def index(request):
def index(request):
    return render(request, "index.html")

def resultado(request, dni):
    return render(request, "resultado.html")

@login_required
def solicitudes(request):
    return render(request, "solicitudes.html")


