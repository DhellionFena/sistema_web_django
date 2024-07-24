from django.urls import path
from . import views

urlpatterns = [
    path('', views.main, name='index'),
    path('users/', views.users, name='usuarios'),
    path('users/detalhes/<int:id>', views.detalhes, name='detalhes'),
]
