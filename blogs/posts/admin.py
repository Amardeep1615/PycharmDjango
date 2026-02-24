from django.contrib import admin
from .models import Post, Comment, Tag


# Register your models here.
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
        list_display = ['title']
        list_filter = ['title','img','desc']
        search_fields = ['title']




admin.site.register(Comment)
admin.site.register(Tag)
