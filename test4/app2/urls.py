from django.urls import path,include

from app2 import views

urlpatterns = [
    path('chack/',views.check,name='chack')
]