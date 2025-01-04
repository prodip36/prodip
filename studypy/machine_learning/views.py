from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def machine_learn(request):
    return render(request,'machine_learning.html')
