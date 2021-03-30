from django.urls import path
from . import views

urlpatterns =[
    path('home', views.home, name='home'),
    path('', views.login, name='login'),
    path('registration', views.registration, name='registration'),
    path('search', views.search, name='search'),
    

]