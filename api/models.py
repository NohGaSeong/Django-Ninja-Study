from django.db import models

class Department(models.Model):
    title = models.CharField(max_length=100)

class Employee(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    depoartment = models.ForeignKey(Department, on_delete=models.CASCADE)
    birthdate = models.DateTimeField(null= True, blank=True)