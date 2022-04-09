from django.shortcuts import render
from .models import Post
from django.core.paginator import Paginator
# Create your views here.
def home(request):
    form = Post.objects.all().order_by('id')
    paginator = Paginator(form,2,orphans=1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    print('all_post',form)
    print()
    print('paginator',paginator)
    print()
    print('page_number',page_number)
    print()
    print('page_obj',page_obj)
    return render(request,'home.html',{'form':page_obj})
