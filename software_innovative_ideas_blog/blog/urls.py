from django.urls import path
from . import views

urlpatterns = [
    path('createaccount/', views.createaccount, name='createaccount'),
    path('addtopic/', views.addtopic, name='addtopic'),
    path('topics/', views.topics, name='topics'),
    path('landing/', views.landing, name='landing'),
    path('login/', views.login, name='login'), 
    path('logout/', views.login, name='logout'), 
    path('main/', views.main, name='main'), 
]