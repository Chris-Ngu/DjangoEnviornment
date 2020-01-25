from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    print (args, kwargs)
    print(request.user)
    return HttpResponse("<h1>Hello There!</h1>")

def contact_view(*args, **kwards):
    return HttpResponse("<h1>Contact page under construction</h1>")