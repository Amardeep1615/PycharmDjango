#
#
# Today topics :
#
# 1.Django Intorduction
#
# 2.Django Installation
# Important Commands
# pip install virtualenv env
# virtualenv env / python -m venv env
# env/scripts/activate
# pip install django
# django-admin
# django-admin startproject blogs
# cd blogs
# python manage.py runserver
# python manage.py startapp posts
# python manage.py runserver
#
# 3.Django Views,HttpResponse,HttpResponseRedirect,render,redirect,reverse,raise 404,HttpResponseNotFound
# blogs/urls (main urls)
# posts/urls (app urls - create manually)
# posts/views (used for the handle the logic)
#
# 4.Django Templates
# templates/base.html (In Blogs Directory)
# templates/posts/home.html (In Posts App
# templates/posts/detail.html (In Posts App)
# urls,staticfiles,names,filters
# Bootstrap
# commands: in settings.py
# DIRS = [ BASE_DIR / 'templates']
# STATICFILES_DIR = [BASE_DIR / 'static']
# Local vs Global static files
# Tags ({% %}) - for,endfor,if,endif,else,empty
# and also extends 'base.html',block title,endblock title,block content,endblock content,load static,
# link href ="url static 'file',block css,endblock css "
#
# Variables - {{}} - to read the data
#
# 5.Django Context_processors
# create a python file in app posts
# define function named sample and write the dictionary values and then return the context
# ___drop down menu----
# now configure
# In settings.py posts(app name).context_processors(file name).sample(function name)
# read the data in the list format in the base.html
# arrange the bootstrap related css to look in the structure format
#
#
#
# 6.Django Models(Intorduction),Migrations,dbsqlite3,sqlite3 (install)
# define class named Post from  django .import models
# class Post(models.Model):
#     title = models.CharField(max_length=200)
#     desc = models.TextField()
#     img = models.URLField())
#     Commands:-
#     python manage.py makemigrations
#     python manage.py showmigrations
#     python manage.py migrate
#
#  Checking...
#        python manage.py sqlmigration posts 0001
#        python manage.py sqlmigration posts 0002
#        python manage.py shell - to activate Interactive console,to read the query set,objects
#
#     from posts.models import Post
#     P = Post(title = "Django Intorduction",desc = "Django is a python web framework ")
#     P.save()
#
#     P = Post.objects.create(title="Python Intorduction",desc="python follows Indentation ")
#
#     from django.db import connection
#     connection.queries
#     Post.objects.all()
#
#     data = Post.objects.all()
#     data
#     data[0].id
#     data[0].title
#     data[0].desc
#
#    for d in data:
#        print(d.id,d.title,d.desc)
#        re-enter here
#
#        print(d.id,d.title,d.desc,Cdate)
#
# 7.Django Lookups and Model API Methods
#
#
#
#
#
#
#
#
#
