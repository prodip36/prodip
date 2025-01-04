from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def deep_learning(request):
    return render(request,'deep_learning.html')