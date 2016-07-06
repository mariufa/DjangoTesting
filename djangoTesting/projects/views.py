from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

from .models import Project

def index(request):
    projectsList = Project.objects.all()
    template = loader.get_template('projects/index.html')
    context = {
        'projectsList': projectsList,
    }
    return HttpResponse(template.render(context, request))
