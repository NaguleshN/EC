from django.shortcuts import render,redirect
from app.models import *

def home(request):
    product= SolarPanel.objects.all()
    return render(request,"home.html",{'product':product})

def description(request,id):
    product= SolarPanel.objects.get(id=id)
    return render(request,"description.html",{'product':product})

def enable_state(request,id):
    product= SolarPanel.objects.get(id=id)
    product.status="Active"
    product.save()
    return redirect("home")

def disable_state(request,id):
    product= SolarPanel.objects.get(id=id)
    product.status="Inactive"
    product.save()
    return redirect("home")

def chart_disp(request):
    return render(request,"chart.html")

def contact(request):
    return render(request,"contact.html")