from django.shortcuts import render
from django.http import HttpResponse


def say_hello(request):
    # can do tasks like get data from db, transform data, email, etc.
    # return HttpResponse("Hello World")
    return render(request, "hello.html", {"name": "Rishabh"})
