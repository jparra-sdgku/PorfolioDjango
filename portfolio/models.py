from django.db import models

# Create your models here.

class Skill(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

    
    


class Project(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    year = models.IntegerField()
    skills = models.ManyToManyField('Skill')
    link = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to='static/img/')
    
    def __str__(self):
        return f'{self.name} - {self.year}'