from django.contrib import admin
from . import models

class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'title', 'courses_count', 'students_count']
    list_filter = ['is_active']

admin.site.register(models.Teacher, TeacherAdmin)
# Register your models here.
