from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def home_view(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello World</h1>")  # string of HTML code
    return render(request, "home.html", {})


def contact_view(request, *args, **kwargs):
    my_context = {
        "title": "This is about us",
        "my_number": 123,
        "my_list": [12, 3434, 312, 23421, 3342, 'Abc'],
        "my_html": "<h1>Hello World</h1>"
    }
    return render(request, "contact.html", my_context)
