from django.contrib import admin
from .models import Post,song
# Register your models here.
@admin.register(Post)
class PostAdminModel(admin.ModelAdmin):
    list_display = ['id','user','post_title','post_cat','post_publish_date']

@admin.register(song)
class songAdminModel(admin.ModelAdmin):
    list_display = ['song_name','song_duration','written_by']