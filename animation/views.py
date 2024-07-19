from django.http import HttpResponse
from django.shortcuts import render
import datetime
# Create your views here.
def index(request):
    now = datetime.datetime.now()
    return render(request, "cashflow/index.html",{
        "newyear": now.month ==1 and now.day == 1 
    })

def greet(request, name):
    return render(request, "cashflow/insert_cashflow.html",{
        "name": name.capitalize()
    })

def distance(request):
    return render(request, "animation.py")