from django.shortcuts import render
from .models import user,techer
# Create your views here.

def get(request):
    # all user get
    form = user.objects.all()
    print(form)
    print('-----------------------------')
    print(form.query)

    # user marks 100 or >70 or <100
    form = user.objects.filter(marks = 100)
    # marks not 100 
    form = user.objects.exclude(marks = 100)

    # order by ( 'asc order'  , '-field' desc order  , '?' - randomly)
    form = user.objects.order_by('marks')
    # form = user.objects.order_by('-marks')
    # form = user.objects.order_by('?marks')
    # form = user.objects.order_by('marks').reverse()[:1]
    form = user.objects.values('marks')
    form = user.objects.values()

    #  list value tuple form show 
    form = user.objects.values_list()
    form = user.objects.values_list('user')
    form = user.objects.values_list('user',named=True)
    form = user.objects.using('default')
    form = user.objects.dates('pass_date','month')
    form = user.objects.dates('pass_date','year')
# 
    q1 = user.objects.values_list('user','city',named=True)
    q2 = techer.objects.values_list('user','city',named=True)
    # show on set format
    # form = q1.union(q2)
    # using all field show include duplicate
    # form = q1.union(q2,all=True)

    form = q1.intersection(q2)

    form = q1.difference(q2)


    ########################### AND  OR OPERATOR ###########################

    form = user.objects.filter(id =2) & user.objects.filter(roll=2) 
    form = user.objects.filter(id =2) | user.objects.filter(roll=1) 



    #################### get #################

    # form = user.objects.get(id = 1)
    # form = user.objects.first()
    # form = user.objects.order_by('roll').first()

    form = user.objects.last()
    form = user.objects.latest('roll')

    
    
    print(form)

    return render(request,'show.html', {'form':form})