from django.contrib import admin
from .models import user
# Register your models here.
@admin.register(user)
class modeladmin(admin.ModelAdmin):
    list_diplay = ( 'name' , 'surname' ,'age' , 'email' , 'DOB' ,'test' )