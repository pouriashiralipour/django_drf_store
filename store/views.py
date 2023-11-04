from django.shortcuts import HttpResponse, render


def say_hello(request):
    return render(request, "home.html")
