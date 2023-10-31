from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import SignupForm, LoginForm, PostForm
from .models import Post_data


# Create your views here.
# Home
def home(request):
    posts = Post_data.objects.all()
    return render(request, 'home.html', {'posts': posts})


# about
def about(request):
    return render(request, 'about.html')


# contact
def contact(request):
    return render(request, 'contact.html')


# Dashboard
def dashboard(request):
    if request.user.is_authenticated:
        post = Post_data.objects.all()
        return render(request, 'dashboard.html', {'post': post})
    else:
        return HttpResponseRedirect('/login/')


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/')


# signup
def user_signup(request):
    if request.method == "POST":
        form = SignupForm(request.POST)
        if form.is_valid():
            messages.success(request, "Congratulations !!! you have sucessfully signup")
            form.save()
    else:
        form = SignupForm()
    return render(request, 'signup.html', {'form': form})


# login
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = LoginForm(request=request, data=request.POST)
            if form.is_valid():
                uname = form.cleaned_data['username']
                upass = form.cleaned_data['password']
                user = authenticate(username=uname, password=upass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in successfully')
                    return HttpResponseRedirect('/dashboard/')
        else:
            form = LoginForm()
        return render(request, 'login.html', {'form': form})
    else:
        return HttpResponseRedirect('/dashboard/')


def addpost(request):
    if request.user.is_authenticated:
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                ti = form.cleaned_data['title']
                de = form.cleaned_data['desc']

                pst = Post_data(title=ti, desc=de)
                pst.save()
                form = PostForm()
            else:
                form = PostForm()

            return render(request, 'addpost.html', {'fr': form})

        else:
            return HttpResponseRedirect('/login/')


def updatepost(request, id):
    if request.user.is_authenticated:
        if request.method == 'POST':
            pi = Post_data.objects.get(pk=id)
            form = PostForm(request.POST, instance=pi)
            if form.is_valid():
                form.save()
            else:
                pi = Post_data.objects.get(pk=id)
                form = PostForm(instance=pi)
        return render(request, 'updatepost.html',{'fr':form})
    else:
        return HttpResponseRedirect('/login/')


def deletepost(request, id):
    if request.user.is_authenticated:
        return HttpResponseRedirect('/dashboard/')
    else:
        return HttpResponseRedirect('/login/')

    # post = Post_data.objects.get(pk=id)
    # post.delete()
    # return HttpResponseRedirect('/home/')

