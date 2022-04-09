from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UserRegi
from .models import User
from django.views.generic.base import TemplateView,RedirectView
from django.views import View

# Create your views here.
class UserAddshowView(TemplateView):
    template_name = 'index.html'
    def get_context_data(self,*args, **kwargs):
        context =super().get_context_data(**kwargs)
        form = UserRegi()
        stud = User.objects.all()
        context = {"stud" : stud ,'form':form}
        return context

    def post(self,request):
        form = UserRegi(request.POST,label_suffix=" ")
        if form.is_valid():
            username = form.cleaned_data['username']
            email  = form.cleaned_data['email']
            password = form.cleaned_data['password']
            roll_no = form.cleaned_data['roll_No']
            regi = User(username=username,email=email,password=password,roll_No=roll_no)
            regi.save()
            return HttpResponseRedirect('/')

class UserUpdateView(View):
    def get(sself,request,id):
        pi = User.objects.get(pk=id)
        form = UserRegi(instance=pi)
        return render(request,'edit.html',{'form':form})
    def post(self,request,id):
        pi = User.objects.get(pk=id)
        form = UserRegi(request.POST, instance=pi)
        if form.is_valid():
            form.save()
        return HttpResponseRedirect('/')

class UserDeleteVieww(RedirectView):
    url = '/'
    def get_redirect_url(self, *args, **kwargs):
        del_id = kwargs['id']
        User.objects.get(pk=del_id).delete()
        return super().get_redirect_url(*args, **kwargs)




    