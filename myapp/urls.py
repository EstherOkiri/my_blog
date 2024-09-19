from django.urls import path
from . import views




urlpatterns = [
    path('', views.helloWorld, name='home'),
    path('about/', views.about, name='about'),
]