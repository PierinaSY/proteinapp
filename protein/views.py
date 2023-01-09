from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

# def home(request):
#     return HttpResponse("Hello, This is an app to query Proteins!")

def home(request):
    return render(request, "protein/index.html")