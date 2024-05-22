from django.contrib import admin
from .models import Project, Task, TaskAssignment, Comment

class ProjectAdmin(admin.ModelAdmin):
    """Admin configuration for the Project model."""
    pass

class TaskAdmin(admin.ModelAdmin):
    """Admin configuration for the Task model."""
    pass

class TaskAssignmentAdmin(admin.ModelAdmin):
    """Admin configuration for the TaskAssignment model."""
    pass

class CommentAdmin(admin.ModelAdmin):
    """Admin configuration for the Comment model."""
    pass

# Registering models with their respective admin configurations
# admin.site.register()used to associate each model with its corresponding admin configuration.
admin.site.register(Project, ProjectAdmin)
admin.site.register(Task, TaskAdmin)
admin.site.register(TaskAssignment, TaskAssignmentAdmin)
admin.site.register(Comment, CommentAdmin) 
