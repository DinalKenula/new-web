from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def home_view(request):
    return render(request, "index.html")


def blog(request):
    return render(request, "blog.html")


def historical(request):
    return render(request, "historical.html")

def exotic(request):
    return render(request, "exoticp.html")
