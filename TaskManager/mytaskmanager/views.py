# views.py
from rest_framework import generics
from .models import Project, Task, TaskAssignment, Comment
from .serializers import ProjectSerializer, TaskSerializer, TaskAssignmentSerializer, CommentSerializer

class ProjectListCreate(generics.ListCreateAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class ProjectDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer

class TaskListCreate(generics.ListCreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

class TaskAssignmentListCreate(generics.ListCreateAPIView):
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

class TaskAssignmentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TaskAssignment.objects.all()
    serializer_class = TaskAssignmentSerializer

class CommentListCreate(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
