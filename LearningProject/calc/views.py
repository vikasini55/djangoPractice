from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Member

def home(request):
    students=Member.objects.all().values()
    template = loader.get_template('home.html')
    context={
        'students':students
    }
    return HttpResponse(template.render(context,request))

def details(request,id):
    student=Member.objects.get(id=id)
    template = loader.get_template('details.html')
    context={
        'student':student
    }
    return HttpResponse(template.render(context,request))

def main(request):
    template = loader.get_template('main.html')
    return HttpResponse(template.render())