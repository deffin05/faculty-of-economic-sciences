from django.db import models

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, blank=True, null=True, related_name='professors')

class Department(models.Model):
    name = models.CharField(max_length=100)
    head = models.ForeignKey('Professor', on_delete=models.SET_NULL, blank=True, null=True, related_name='departments')

class Major(models.Model):
    name = models.CharField(max_length=100)
    code = models.CharField(max_length=100)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=100)
    coordinator_contact = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

class Subject(models.Model):
    major = models.ForeignKey('Major', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)