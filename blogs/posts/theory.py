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
# 6.Django Templates
# templates/base.html (In Blogs Directory)
# templates/posts/home.html (In Posts App
# templates/posts/detail.html (In Posts App)

# 7.Django urls,staticfiles,names,filters
# Bootstrap
# commands: in settings.py
# DIRS = [ BASE_DIR / 'templates']
# STATICFILES_DIR = [BASE_DIR / 'static']

# 8.Django Local vs Global static files and variables ,tags
# Tags ({% %}) - for,endfor,if,endif,else,empty
# and also extends 'base.html',block title,endblock title,block content,endblock content,load static,
# link href ="url static 'file',block css,endblock css "
# Variables - {{}} - to read the data
#
# 9.Django Context_processors
# create a python file in app posts
# define function named sample and write the dictionary values and then return the context
# ___drop down menu----
# now configure
# In settings.py posts(app name).context_processors(file name).sample(function name)
# read the data in the list format in the base.html
# arrange the bootstrap related css to look in the structure format
#

# 10.Django Models(Intorduction),Migrations,dbsqlite3,sqlite3 (install)
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

# 11.Django Models,Migrations,save and create

# 12.Django Lookups and Model API Methods

# 13.Django OrderBy,Reverse,Aggregate,Updating

# 14.Django CreatingSuperUser Admin Panel

# 15.Django Model Forms

# 16.Django ModelForms,Arguments,Outputtypes and forms in loops

# 17.Django Custom Form Validations

# 18.Django Connecting Custom Forms And Models

# 19.Django Create,Read,Update,Delete (CRUD) Forms

# 20.Django ModelForms ...

# 21.Django Cookies

# 22.Django Middlewares

# 23.Django Session

# 24.Django Authorization

# 25.Django LoginForm

# 26.Django Limiting User Authentications

# 27.Django Build-in Views

# 28.Django Pagination

# 29.Django Relations
#     One to One Relationship
#     forms.py create a form
#     models.py create a model
#     admin.site.register(relation)
#     Husband and Wife relationship
#     Note: Practical-admin Panel - 1.models.on delete=CASCADE,2.models.Protect,3.models.SET_NULL,null=True
#
# 30.Django Many to one and Many to Many Relations
#      1.Many to One Relation
#      define comment form in models.py and import comment form in forms.py ,make migrations and now define a class named CommentForm
#      write the model and fields in meta defined in the class,exclide the Posts
#      2.Modify the views in details where the coment must render in it and add the related code in the details.html
#      3.Check the submit data in Admin Panel
#      4.Coment store and display in the interface
#      5.To see the previous comments add thecode if state in details.html
#      6.Do more practice in this Relationships
#
#      2.Many to Many Relation
#      1.define Tag form in models.py and import Tag form in forms.py,make migrations and now define a class named TagForm
#      write the model and fileds in meta define in the classmethod
#      2.Modify the views in details where the coment must render in it and add the related code in the details.html
#      3.Check the submit data in Admin Panel
#      4.Tag store and display in the interface
#      5.To see the previous comments add thecode if state in details.html
#      6.Do more practice in this Relationships
# #
# #
#
#
#
#
#
