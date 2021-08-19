from django.db import models

# Create your models here.
class Student():
    name = models.CharField(max_length=20)