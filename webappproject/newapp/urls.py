
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('image-recognition', views.analyze, name="analyze"),
    path('camera', views.photo, name="photo"),
    path('files', views.file, name="file"),
    path('numbers', views.number, name="numbers"),
    path('train', views.train_model, name="train")
]