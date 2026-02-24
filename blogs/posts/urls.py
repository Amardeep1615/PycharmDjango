
from django.urls import path
from .import views
from django.contrib import admin

urlpatterns = [
    path('home/',views.home, name='home'),
    path('detail/<int:id>/',views.detail,name='detail'),
]
admin.site.site_title = 'My Courses Blog'
admin.site.site_header = 'MY COURSES'
admin.site.index_title = 'My Posts List'
