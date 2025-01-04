from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def machine_learning(request):
    return HttpResponse('<h2>This a simple django project. Now i can create a django server.</h2>')

def deep_learning(request):
    return HttpResponse('This is another http response.')
def about_me(request):
    return HttpResponse('<h3>Name:Prodip sarker <br>Dist:Tangail</h3>')