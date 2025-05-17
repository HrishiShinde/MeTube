from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('watch/<int:id>/', views.watch, name='watch'),
    path('upload/', views.upload, name='upload'),
]