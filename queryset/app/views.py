from django.shortcuts import render
from .models import user,techer
from django.db.models import Avg,Min,Max,Sum,Count
from django.db.models import Q
# Create your views here.

def get(request):
    # all user get
    form = user.objects.all()
#     print(form)
#     print('-----------------------------')
#     print(form.query)

#     # user marks 100 or >70 or <100
#     form = user.objects.filter(marks = 100)
#     # marks not 100 
#     form = user.objects.exclude(marks = 100)

#     # order by ( 'asc order'  , '-field' desc order  , '?' - randomly)
#     form = user.objects.order_by('marks')
#     # form = user.objects.order_by('-marks')
#     # form = user.objects.order_by('?marks')
#     # form = user.objects.order_by('marks').reverse()[:1]
#     form = user.objects.values('marks')
#     form = user.objects.values()

#     #  list value tuple form show 
#     form = user.objects.values_list()
#     form = user.objects.values_list('user')
#     form = user.objects.values_list('user',named=True)
#     form = user.objects.using('default')
#     form = user.objects.dates('pass_date','month')
#     form = user.objects.dates('pass_date','year')
# # 
#     q1 = user.objects.values_list('user','city',named=True)
#     q2 = techer.objects.values_list('user','city',named=True)
#     # show on set format
#     # form = q1.union(q2)
#     # using all field show include duplicate
#     # form = q1.union(q2,all=True)

#     form = q1.intersection(q2)

#     form = q1.difference(q2)


#     ########################### AND  OR OPERATOR  Q Object ###########################

#     form = user.objects.filter(id =2) & user.objects.filter(roll=2) 
#     form = user.objects.filter(id =2) | user.objects.filter(roll=1) 



#     #################### get #################

#     # form = user.objects.get(id = 1)
#     # form = user.objects.first()
#     # form = user.objects.order_by('roll').first()

#     form = user.objects.last()
#     form = user.objects.latest('roll')
#     form = user.objects.earliest('pass_date')

#     form = user.objects.all()
#     print(form.exists())
#     one_data = user.objects.get(pk=1)
#     print(form.filter(pk=one_data.pk).exists())

#     #form = user.objects.create(user= 'hh',roll = 104 ,city = 'surat' marks = 78 , pass_date = '2022-5-4')
    
#     form = user.objects.get_or_create( user = 'hh',roll = 200 ,city = 'surat', marks = 78 , pass_date = '2022-5-4')

#     form  = user.objects.filter(id=3).update(user = 'harish', marks = 98)
#     form  = user.objects.filter(marks=70).update(marks = 80)

    # form, create = user.objects.update_or_create(id=14, user='sameer',roll=15,defaults={'user':'harish','roll':89,'marks':56,'pass_date':'2022-05-14'})
    # print(create)
    # obj = [
    #     user(user='sonal',roll=120,city='dhandad',marks=40,pass_date='2020-05-04'),
    #     user(user='arjun',roll=121,city='dhandad',marks=40,pass_date='2020-05-04'),
    # ]
    # form = user.objects.bulk_create(obj)

    # all_user_data = user.objects.all()
    # for stu in all_user_data:
    #     stu.city = 'dhanbad'
    #     form = user.objects.bulk_update(all_user_data,['city'])

    # form = user.objects.in_bulk([1,2])
    # print(form[2].user)
    # form = user.objects.in_bulk([1,2])

    # form = user.objects.get(pk=4).delete()
    # form = user.objects.filter(marks=100).delete()
    # form = user.objects.all().delete()
    # form = user.objects.all()
    # print(form.count())
    # form = user.objects.all().explain()

    ##########################################################################################################################


    form = user.objects.filter(user__exact = 'arjun')
    form = user.objects.filter(user__iexact = 'Arjun')
    form = user.objects.filter(user__contains = 'arjun')
    form = user.objects.filter(user__icontains = 'arjun')
    form = user.objects.filter(id__in = [1,5,8])
    form = user.objects.filter(marks__in = [80])
    form = user.objects.filter(user__startswith = 'arjun')
    form = user.objects.filter(user__istartswith = 'arjun')
    form = user.objects.filter(user__endswith = 'n')
    form = user.objects.filter(user__iendswith = 'n')

    # form = user.objects.filter(passdate__range = (('2022,1,4'),('2020-05-03'))  precticee  learnnnnn....
    # form = user.objects.filter(admdatetime__date = date(2022,1,4))  precticee  learnnnnn....
    
    # form = user.objects.filter(admdatetime__date__gt = date(2022,1,4))  precticee  learnnnnn....
    # form = user.objects.filter(pass_date__year=2022)#  precticee  learnnnnn....
    # form = user.objects.filter(pass_date__year__gte=2022)
    # form = user.objects.filter(pass_date__month=4)
    # form = user.objects.filter(pass_date__month__gt=4)
    # form = user.objects.filter(pass_date__day=2)
    # form = user.objects.filter(pass_date__day__gt=2)
    # form = user.objects.filter(pass_date__week=14)
    # form = user.objects.filter(pass_date__week_day=5)
    # form = user.objects.filter(pass_date__week_day__gt=5)
    # form = user.objects.filter(pass_date__quarter=2)
    

    # date and time field use
    # form = user.objects.filter(admdatetime__time__gt = time(21,17))
    # form = user.objects.filter(admdatetime__hour__gt = 5)
    # form = user.objects.filter(admdatetime__minute__gt = 26)
    # form = user.objects.filter(admdatetime__second__gt = 26)
    form = user.objects.filter(roll__isnull = False) # or True
    

    form = user.objects.all()
    avg = form.aggregate(Avg('marks'))
    min = form.aggregate(Min('marks'))
    max = form.aggregate(Max('marks'))
    sum = form.aggregate(Sum('marks'))
    count = form.aggregate(Count('marks'))
    # print(avg)
    

############################## Q object ##############################

    # form = user.objects.filter(Q(id=2)&Q(roll=2))
    # form = user.objects.filter(Q(id=2)|Q(roll=2))
    # form = user.objects.filter(~Q(id=2))
    
###########################limit Queryset in django######################
    form =  user.objects.all()[:5]
    form =  user.objects.all()[5:8]
    form =  user.objects.all()[::2]

   


    # print(form)

    return render(request,'show.html', {'form':form,'avg':avg,'min':min,'max':max,'sum':sum,'count':count})