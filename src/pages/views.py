from django.shortcuts import render
from django.http import HttpResponse

def home_view(request, *args, **kwargs):
    print (args, kwargs)
    print(request.user)
    #return HttpResponse("<h1>Hello There!</h1>")
    return render(request, "home.html", {})

def contact_view(request, *args, **kwargs):
    return render(request, "contact.html", {})

def about_view(request, *args, **kwargs):
    my_context = {
        "my_text" : "this is about us",
        "my_number" : 123,
        "my_list" : [123, 455, 665, "Abc"],
        "my_html": "<h1>html tester</h1>"
    }

    return render(request, "about.html", my_context)
    
