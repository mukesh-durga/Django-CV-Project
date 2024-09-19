from django.urls import path
from .views import resume_view
from . import views

urlpatterns = [
    path('', resume_view, name='resume'),
    path('', views.home_view, name='home'),  
    path('resume/', views.resume_view, name='resume'),   
]
