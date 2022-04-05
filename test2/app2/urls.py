from django.urls import path
from . import views
# from app2 import views

urlpatterns = [
    path('add/ ',views.check,name='check'),
]
