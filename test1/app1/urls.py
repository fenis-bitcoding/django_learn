from django.contrib import admin
from django.urls import path,include
from app1 import views
# from app2 import views



urlpatterns = [
    path('',views.home,name='home'),
    path('index/',views.index,name='index'),
]
