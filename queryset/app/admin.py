from django.contrib import admin
from .models import user,techer
# Register your models here.
@admin.register(user)
class useradmin(admin.ModelAdmin):
    list_display = [ 'id' , 'user' , 'roll' , 'city' , 'marks' , 'pass_date']   

@admin.register(techer)
class techaradmin(admin.ModelAdmin):
    list_display = [ 'id' , 'user' , 'empnum' , 'city' , 'salary' , 'join_date']   