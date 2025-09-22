from django.contrib import admin

from faculty.models import Subject, Department, Professor, Major


# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'head']

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'department']

class MajorAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'coordinator_name', 'department']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Major, MajorAdmin)
