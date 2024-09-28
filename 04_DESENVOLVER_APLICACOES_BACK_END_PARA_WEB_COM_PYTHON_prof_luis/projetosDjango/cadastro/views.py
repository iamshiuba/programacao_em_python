from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    return HttpResponse("Estou na Web!!!")

def segundo(request):
    return HttpResponse("<h1>Segunda</h1>")