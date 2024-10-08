
# students/models.py
from django.db import models

class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=10, unique=True)
    email = models.EmailField()
    date_of_birth = models.DateField()
    
    def __str__(self):
        return self.name
