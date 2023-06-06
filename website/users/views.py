from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import My_User


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            request.session['person'] = {'username': username}
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Wrong username or password..."))
            return redirect('login')
    else:
        return render(request, 'authentication/login.html', {})


def logout_user(request):
    logout(request)
    return redirect('index')

def register_user(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('index')
        else:
            messages.success(request, ("Wrong username or password..."))
    else:
        form = UserCreationForm()

    return render(request, 'authentication/register.html', {
        'form':form
    })

def profile(request):
    list = My_User.objects.all()
    username = ' '
    name = ' '
    surname = ' '
    phone = ' '
    date_of_birth = ' '
    email = ' '
    for i in list:
        if str(i.username) == request.session['person']['username']:
            username = i.username
            name = i.name
            surname = i.surname
            phone = i.phone
            date_of_birth = i.date_of_birth
            email = i.email
    if request.method == "POST":
        
    return render(request, 'statistics/profile.html', {
        "username": username,
        "name": name,
        "surname": surname,
        "phone": phone,
        "date_of_birth": date_of_birth,
        "email": email
    })

def adminpage(request):
    list = My_User.objects.all()
    username = ' '
    name = ' '
    surname = ' '
    phone = ' '
    date_of_birth = ' '
    email = ' '
    for i in list:
        if str(i.username) == request.session['person']['username']:
            username = i.username
            name = i.name
            surname = i.surname
            phone = i.phone
            date_of_birth = i.date_of_birth
            email = i.email
    return render(request, 'statistics/adminpage.html', {
        "username": username,
        "name": name,
        "surname": surname,
        "phone": phone,
        "date_of_birth": date_of_birth,
        "email": email
    })

