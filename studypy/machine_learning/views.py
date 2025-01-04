from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.
def machine_learn(request):
    #django variables
    name='Prodip Sarker'
    age=25
    dist='Tangail'
    uni= 'Mbstu'
    phn='+8801860931442'
    offering = {'name':name,'age':age,'dist':dist,'uni':uni,'phn':phn}
    return render(request,'machine_learning/machine_learning.html',context=offering)

def knn(request):
    return render(request,'machine_learning/knn.html')

def rand(request):
    return render(request,'machine_learning/random.html')

def robo(request):
    return render(request,'machine_learning/robot.html')

