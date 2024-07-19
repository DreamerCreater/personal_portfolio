from django.shortcuts import render
import datetime

def index(request):
    now = datetime.datetime.now()
    is_newyear = now.month == 1 and now.day == 1

    # Dynamic spacing (example: 50px distance for non-New Year's, 0px for New Year's)
    spacing = '0px' if is_newyear else '50px'
    
    return render(request, "cashflow/index.html", {
        "newyear": is_newyear,
        "spacing": spacing
    })

def greet(request, name):
    return render(request, "cashflow/insert_cashflow.html", {
        "name": name.capitalize()
    })

def distance(request):
    # You might want to return a response or render a template here
    return HttpResponse("Distance view is not implemented.")
