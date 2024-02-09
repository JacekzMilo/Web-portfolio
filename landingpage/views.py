from django.shortcuts import render
from .models import Project


def items(request):
    projects = Project.objects.all().order_by('Project_no') # zwraca wszystkie obiekty w danej bazie danych
    return render(request, 'index.html', {'projects': projects})


def index(request): # nazwane index ale moze byc jakkolwiek inaczej, to jest powitalna strona argument to request http (wywolanie strony)
    projects = Project.objects.all().order_by('Project_no')
    return render(request, 'landingpage.html', {'projects': projects})  # zwracamy obiekt, tworzymy instancje obiektu


def new(request):
    return render(request, 'about_me.html')



# .filter(Project_name="Web-Portfolio")