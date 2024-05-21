from django.db import models
from django.contrib.auth.models import User

class Project(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()

class Task(models.Model):
    STATUS_CHOICES = [
        ('to-do', 'To Do'),
        ('in-progress', 'In Progress'),
        ('completed', 'Completed')
    ]
    name = models.CharField(max_length=255)
    description = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES)
    priority = models.IntegerField()
    deadline = models.DateField()
    project = models.ForeignKey(Project, on_delete=models.CASCADE)

class TaskAssignment(models.Model):
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

class Comment(models.Model):
    commenter_name = models.CharField(max_length=255)
    email = models.EmailField()
    content = models.TextField()
    task = models.ForeignKey(Task, on_delete=models.CASCADE)
