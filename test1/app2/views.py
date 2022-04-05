from django.shortcuts import render

# Create your views here.
def app2(request):
    return render(request, 'ap2/app2.html')