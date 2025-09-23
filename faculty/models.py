from django.db import models

# Create your models here.

class Professor(models.Model):
    name = models.CharField(max_length=200)
    position = models.CharField(max_length=100)
    degree = models.CharField(max_length=100)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True, related_name='professors')

class Department(models.Model):
    name = models.CharField(max_length=200)
    head = models.CharField(max_length=200, null=True)

class Major(models.Model):
    name = models.CharField(max_length=200)
    code = models.CharField(max_length=10)
    description = models.TextField()
    coordinator_name = models.CharField(max_length=200)
    coordinator_contact = models.CharField(max_length=50)
    department = models.ForeignKey('Department', on_delete=models.SET_NULL, null=True)

    def get_short_description(self):
        if len(self.description.split()) > 50:
            return ' '.join(self.description.split()[:50]) + "..."
        else:
            return self.description

class Subject(models.Model):
    major = models.ForeignKey('Major', on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
