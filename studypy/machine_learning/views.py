from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine_learning(request):
    return HttpResponse('<h2>This a simple django project.</h2>')
