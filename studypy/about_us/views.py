from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def about(request):
    return render(request,'about_us/about_us.html')
