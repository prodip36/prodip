
from django.urls import path
from . import views
urlpatterns = [
     path('ml/',views.machine_learn),
     path('knn/',views.knn),
     path('rand/',views.rand),
     path('robo/',views.robo),
    

]
