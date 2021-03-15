from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home_page(request, *args, **kwargs):
    # return HttpResponse("<h1>Hello User<h1>")
    print(args, kwargs)
    print(request.user)
    return render(request, "home.html", {})


def turn_page(request, *args, **kwargs):
    return render(request, "turn_page.html", {})


def contact_us_page(request, *args, **kwargs):
    return render(request, "contact_us.html", {})


def faq_page(request, *args, **kwargs):
    return render(request, "FAQ.html", {})