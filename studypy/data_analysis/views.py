from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def data_ana(request):
    return HttpResponse('<h2>This is data analysis platform</h2>')
