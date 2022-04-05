from django.shortcuts import render
from .forms import UserRegistration
# Create your views here.
def home(request):
    fm = UserRegistration()
    return render(request, 'registrations.html',{'fm':fm})