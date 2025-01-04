from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def blog1(request):
    return HttpResponse('<h4>This is my first blog.<br>Thank you:)</h4>')