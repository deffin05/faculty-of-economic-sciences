from django.http import HttpResponse
from django.shortcuts import render

from faculty.models import Department, Major
# Create your views here.

def index(request):
    return render(request, 'faculty/index.html')

def get_departments(request):
    departments = Department.objects.all()
    return render(request, 'faculty/departments.html', {'departments': departments})

def get_department(request, department_id):
    return render(request, 'faculty/department.html')

def get_programs(request):
    programs = Major.objects.all()
    return render(request, 'faculty/programs.html', {'programs': programs})

def get_program(request, program_id):
    return render(request, 'faculty/program.html')
