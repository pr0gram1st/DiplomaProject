from django.shortcuts import render
from users.models import Course

def home(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def courses(request):
    list = Course.objects.all()
    return render(request, 'courses.html', {'list' : list})

def quiz(request):
    return render(request, 'quiz.html')

