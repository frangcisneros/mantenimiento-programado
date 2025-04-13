from django.shortcuts import render
from api.models import Pieza


def home(request):
    return render(request, "home.html")


def dashboard(request):
    return render(request, "dashboard.html")


def reports(request):
    return render(request, "reports.html")


def settings(request):
    return render(request, "settings.html")


def other(request):
    return render(request, "other.html")
