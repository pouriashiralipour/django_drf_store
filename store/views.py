from django.shortcuts import HttpResponse, render


def say_hello(request):
    name = "pouria"
    return render(
        request,
        "home.html",
        {
            "name": name,
        },
    )
