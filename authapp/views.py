from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login, logout

from mainapp.views import dashboard

# Create your views here.

def view_index(request):
    return render(request,'index.html')

def view_login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username, password = password)
        if user is not None:
            login(request,user)
            return redirect('dashboard')
        else:
            return HttpResponse('Invalid credential')

    return render(request,'login.html')


def view_register(request):
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if(password1 == password2):
            user = User.objects.create_user(username,email,password1)
            return redirect('index')
        else:
            return HttpResponse("password didn't metch")

    return render(request, 'register.html')


def view_logout(request):
    logout(request)
    return redirect('index')