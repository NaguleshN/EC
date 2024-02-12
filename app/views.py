from django.shortcuts import render
from app.models import *
# Create your views here.

def home(request):
    product= SolarPanel.objects.all()
    return render(request,"home.html",{'product':product})

def description(request,id):
    product= SolarPanel.objects.get(id=id)
    return render(request,"description.html",{'product':product})