from django.shortcuts import render

# Create your views here.
def setsession(request):
    request.session['name'] = 'Sonam'
    return render(request,'student/setsession.html')

def getsession(request):
    name = request.session.get('name')
    keys = request.session.keys()
    return render(request,'student/getsession.html',{'name':name,'keys':keys})

def delsession(request):
    if 'name' in request.session:
        del request.session['name']
    return render(request,'student/delsession.html')