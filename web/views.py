from django.shortcuts import render
from api.models import Pieza


def home(request):
    return render(request, "home.html")
