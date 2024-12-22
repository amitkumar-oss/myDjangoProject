from django.contrib import admin
from django.urls import path
from myapp import views

urlpatterns = [
    
    path('',views.home,name='home'),
    path('about/',views.about,name='about'),
    path('contact/',views.contact,name='contact'),
    path('services/',views.services,name='services'),
    path('form/',views.form,name='form'),
    path('submitform/',views.submitform,name='submitform'),
    path('calculator/',views.calculator,name='calculator'),
    path('evenodd/',views.evenodd,name='evenodd'),
    path('marksheets/',views.marksheets,name='marksheets'),
    
    

]