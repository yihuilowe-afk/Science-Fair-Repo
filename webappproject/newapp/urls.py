
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('image-recognition', views.analyze, name="analyze"),
    path('camera', views.photo, name="photo"),
    path('files', views.file, name="file"),
    path('numbers', views.number, name="numbers"),
    path('train', views.train_model, name="train"),
    path('option-2', views.op2, name="possibility-2"),
    path('option-3', views.op3, name="possibility-3"),
    path('option-4', views.op4, name="possibility-4")
]