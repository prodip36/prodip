from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def about(request):
    return HttpResponse('<h1>Hey we are developing a django projects.</h1><br>cont@ct us: +8801860931442<br>all rights reserved.')
