from django.shortcuts import render
from django.http import HttpResponse
from .models import Post
# Create your views here.
posts = [

    {
        'id': 1,
        'img': 'https://upload.wikimedia.org/wikipedia/commons/c/c3/Python-logo-notext.svg',
        'title': 'Python',
        'desc': 'Python is a programming language'
    },
    {
        'id': 2,
        'img': 'https://upload.wikimedia.org/wikipedia/en/3/30/Java_programming_language_logo.svg',
        'title': 'Java',
        'desc': 'Java is an object oriented programming language'
    },
    {
        'id': 3,
        'img': 'https://upload.wikimedia.org/wikipedia/commons/6/61/HTML5_logo_and_wordmark.svg',
        'title': 'Html',
        'desc': 'Html is a Markup language'
    },
    {
        'id': 4,
        'img': 'https://upload.wikimedia.org/wikipedia/commons/d/d5/CSS3_logo_and_wordmark.svg',
        'title': 'Css',
        'desc': 'Css is used to add styles to web pages'
    },
    {
        'id': 5,
        'img': 'https://upload.wikimedia.org/wikipedia/commons/6/6a/JavaScript-logo.png',
        'title': 'JavaScript',
        'desc': 'JavaScript is used to build dynamic web pages'
    },
    {
        'id': 6,
        'img': 'https://upload.wikimedia.org/wikipedia/commons/a/a7/React-icon.svg',
        'title': 'React js',
        'desc': 'React js is used to build single page applications'
    }
]
def home(request):


    return render(request,'posts/home.html',{'posts':posts})

def detail(request,id):
    posted_id = ''
    for post in posts:
        if post['id'] == id:
            posted_id = post

    return render(request,'posts/details.html',{'post': posted_id})