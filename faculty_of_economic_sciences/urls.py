"""
URL configuration for faculty_of_economic_sciences project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

from faculty.views import index, get_departments, get_programs, get_department, get_program

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index, name='index'),
    path('departments/', get_departments, name='departments'),
    path('departments/<int:department_id>/', get_department, name='departments'),
    path('programs/', get_programs, name='programs'),
    path('programs/<int:program_id>', get_program, name='programs'),
]
