from django.contrib import admin
from .models import Project, Task, TaskAssignment, Comment

admin.site.register(Project)
admin.site.register(Task)
admin.site.register(TaskAssignment)
admin.site.register(Comment)
