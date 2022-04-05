from django.shortcuts import render
from .forms import UserRegi
# Create your views here.
def home(request):
    form = UserRegi(auto_id=True,label_suffix=" ",initial={'name':'fenis','email':'gg@gmail.com'})
    form.order_fields(field_order=['email','name'])          
    return render(request,'first.html',{'form':form})