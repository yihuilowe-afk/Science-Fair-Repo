
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('image-recognition', views.analyze, name="analyze"),
    path('photo-input', views.photo, name="photo"),
    path('numbers', views.number, name="numbers")
]