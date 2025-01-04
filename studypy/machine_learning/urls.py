
from django.urls import path
from . import views
urlpatterns = [
    path('ml/',views.machine_learn),
    path('dl/',views.deep_learning),
    path('about/',views.about_me),

]
