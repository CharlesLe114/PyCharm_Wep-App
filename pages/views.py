from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, "index.html", {})


def contact_view(*args, **kwargs):
    return HttpResponse("<h1>Contact Page</h1>")