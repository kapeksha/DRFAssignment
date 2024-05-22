
##serializers are classes that provide way to control how complex data types, like querysets&model instances
##They allows to translate data in your Django models into formats like JSON or XML, which can rendered into HTTP responses.


from rest_framework import serializers
from .models import Project, Task, TaskAssignment, Comment

class ProjectSerializer(serializers.ModelSerializer):
    """
    Serializer for Project model.
    """
    class Meta:
        model = Project
        fields = '__all__'

class TaskSerializer(serializers.ModelSerializer):
    """
    Serializer for Task model.
    """
    class Meta:
        model = Task
        fields = '__all__'

class TaskAssignmentSerializer(serializers.ModelSerializer):
    """
    Serializer for TaskAssignment model.
    """
    class Meta:
        model = TaskAssignment
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    """
    Serializer for Comment model.
    """
    class Meta:
        model = Comment
        fields = '__all__'
