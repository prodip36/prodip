from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def machine_learn(request):
    return render(request,'machine_learning/machine_learning.html')

def knn(request):
    return render(request,'machine_learning/knn.html')

def rand(request):
    return render(request,'machine_learning/random.html')

def robo(request):
    return render(request,'machine_learning/robot.html')

