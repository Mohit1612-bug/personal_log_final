from django.contrib import admin
from .models import Task
# Register your models here.

class TaskAdmin(admin.ModelAdmin):
    list_display=('task_name','task_description','task_status',"due_date")

admin.site.register(Task,TaskAdmin)

# class InformationAdmin(admin.ModelAdmin):
#     list_display=('name','reg_no',"college_name","year","cgpa")
# admin.site.register(Information,InformationAdmin)
