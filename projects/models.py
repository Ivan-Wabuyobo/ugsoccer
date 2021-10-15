from django.db import models
from django.db.models.fields import CharField, FilePathField

class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    technology = models.CharField(max_length=20)
    image = models.CharField(max_length=250)
    
