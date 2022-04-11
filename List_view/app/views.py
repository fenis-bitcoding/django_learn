from django.shortcuts import render
from django.http.response import HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

from .forms import ContractForm

from app.models import student
 # Create your views here.
class StudentListView(ListView):
    model = student
    template_name = 'student.html'

class Studentdetail(DetailView):
    model = student
    template_name = 'school.html'

class ContactFormView(FormView):
    template_name = 'contact.html'
    form_class = ContractForm
    success_url ='/thenkyou/'
    def form_valid(self,form):
        print(form.cleaned_data["name"])
        print(form.cleaned_data["email"])
        print(form.cleaned_data["password"])
        return HttpResponse("Thank You For register bro!!!!!!!!!")

class thankstemplatesView(TemplateView):
    template_name = 'thenkyou.html'