from django.urls import path
from Portfolio import views

urlpatterns = [
    path('', views.homepage, name='homepage'),
    path('home', views.homepage, name='homepage')
]