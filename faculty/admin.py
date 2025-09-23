from django.contrib import admin

from faculty.models import Subject, Department, Professor, Major, MainPage


# Register your models here.

class DepartmentAdmin(admin.ModelAdmin):
    list_display = ['name', 'head']

class ProfessorAdmin(admin.ModelAdmin):
    list_display = ['name', 'position', 'department']

class MajorAdmin(admin.ModelAdmin):
    list_display = ['code', 'name', 'coordinator_name', 'department']

class SubjectAdmin(admin.ModelAdmin):
    list_display = ['name']

class MainPageAdmin(admin.ModelAdmin):

    def has_add_permission(self, request):
        return False if self.model.objects.count() > 0 else super().has_add_permission(request)

admin.site.register(Department, DepartmentAdmin)
admin.site.register(Subject, SubjectAdmin)
admin.site.register(Professor, ProfessorAdmin)
admin.site.register(Major, MajorAdmin)
admin.site.register(MainPage, MainPageAdmin)
