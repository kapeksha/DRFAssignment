##queryset attribute specifies queryset used to retrieve data from database.
##serializer_class attribute specifies serializer class used to serialize or deserialize data for view.



from rest_framework import generics
from .models import Project, Task, TaskAssignment, Comment
from .serializers import ProjectSerializer, TaskSerializer, TaskAssignmentSerializer, CommentSerializer

class ProjectListCreate(generics.ListCreateAPIView):
    """
    API view to list all projects or create a new project.
    """
    queryset = Project.objects.all()  # retrieves all projects from db
    serializer_class = ProjectSerializer  # serializer for Project instances

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a project instance.
    """
    queryset = Project.objects.all()  # retrieves all projects
    serializer_class = ProjectSerializer  # Project instances

class TaskListCreate(generics.ListCreateAPIView):
    """
    API view to list all tasks or create a new task.
    """
    queryset = Task.objects.all()  # tasks
    serializer_class = TaskSerializer  # Task instances

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a task instance.
    """
    queryset = Task.objects.all()  # tasks
    serializer_class = TaskSerializer  # Task instances

class TaskAssignmentListCreate(generics.ListCreateAPIView):
    """
    API view to list all task assignments or create a new task assignment.
    """
    queryset = TaskAssignment.objects.all()  # all task assignments
    serializer_class = TaskAssignmentSerializer  # TaskAssignment instances

class TaskAssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a task assignment instance.
    """
    queryset = TaskAssignment.objects.all()  # all task assignments
    serializer_class = TaskAssignmentSerializer  # TaskAssignment instances

class CommentListCreate(generics.ListCreateAPIView):
    """
    API view to list all comments or create a new comment.
    """
    queryset = Comment.objects.all()  # retrieves all comments
    serializer_class = CommentSerializer  # Comment instances

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    API view to retrieve, update, or delete a comment instance.
    """
    queryset = Comment.objects.all()  # retrieves all comments
    serializer_class = CommentSerializer  # Comment instances
