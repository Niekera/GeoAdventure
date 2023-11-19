from django.shortcuts import render
import random
# Create your views here.

def start_project(request):

    return render(request,"maps/maps_main.html")

   