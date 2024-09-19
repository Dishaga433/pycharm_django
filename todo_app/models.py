from django.db import models

# Create your models here.

class Todo1(models.Model):

    title = models.CharField(max_length=10)
    description = models.CharField(max_length=50)
    date = models.DateField()
