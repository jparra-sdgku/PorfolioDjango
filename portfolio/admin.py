from django.contrib import admin
from .models import Project, Skill
#from . import models


# Register your models here.
admin.site.register(Project)
admin.site.register(Skill)

#admin.site.register(models.Project)
#admin.site.register(models.Skills)


