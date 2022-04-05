from django.shortcuts import render
from .forms import UserRegi
# Create your views here.
def home(request):
    fm = UserRegi(auto_id=True,label_suffix=" ",initial={'name':'fenis','email':'gg@gmail.com'})
    return render(request,'reg.html',{'fm':fm})  