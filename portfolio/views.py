from django.shortcuts import render
from . import models

# Create your views here.
# def projects_list_view(request):
#     return render(request, 'portfolio/projects_list.html')

def projects_list_view(request):
    projects_list = models.Project.objects.all().order_by('-year')
    context = {'projects': projects_list}
    return render(request, 'portfolio/projects_list.html', context)

