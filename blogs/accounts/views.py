from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse
from django.contrib.auth import authenticate,login,logout
from .forms import RegistrationForm,LoginForm


# Create your views here.
def register(request):
    if  request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return HttpResponseRedirect(reverse('home'))
        else:
            form = RegistrationForm()
            return render(request,'accounts/register.html',{'form':form})

def auth_login(request):
    if request.user.is_authenticated:
        return HttpResponseRedirect(reverse('home'))
    else:
         if request.method == 'POST':
          form = LoginForm(request=request,data = request.POST)
          if form.is_valid():
              username = form.cleaned_data.get('username')
              password = form.cleaned_data.get('password')
              user = authenticate(request, username = username, password = password)

              if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('home'))

         form = LoginForm()
         return render(request,'accounts/login.html',{'form':form})


def auth_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('login'))




