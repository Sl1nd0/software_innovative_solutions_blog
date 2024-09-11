from django.urls import path
from . import views

urlpatterns = [
    path('createaccount/', views.createaccount, name='createaccount'),
    path('addtopic/', views.addtopic, name='addtopic'),
    path('addidea/<int:userid>', views.addidea, name='addidea'),
    path('topics/<int:userid>', views.topics, name='topics'),
    path('edittopic/<int:id>', views.edittopic, name='edittopic'),
    path('deletetopic/<int:id>', views.deletetopic, name='deletetopic'),
    path('landing/', views.landing, name='landing'),
    path('landing/<int:id>', views.main_landing, name='main_landing'),
    path('login/', views.login, name='login'), 
    path('logout/', views.login, name='logout'), 
    path('main/', views.main, name='main'), 
]