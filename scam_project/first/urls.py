from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('about/',views.about, name = 'first-about'),
    path('message/',views.message,name ='first-message'),
    path('website/',views.website,name ='first-website'),
    path('',views.home, name = 'first-home')
]