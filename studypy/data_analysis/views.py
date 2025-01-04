from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def data_ana(request):
    return render(request,'data_analysis.html')
