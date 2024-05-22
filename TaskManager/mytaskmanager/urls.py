from django.urls import path
from .views import (
    ProjectListCreate, ProjectDetail,
    TaskListCreate, TaskDetail,
    TaskAssignmentListCreate, TaskAssignmentDetail,
    CommentListCreate, CommentDetail
)

urlpatterns = [
    # URL patterns for projects
    path('projects/', ProjectListCreate.as_view(), name='project-list-create'),
    path('projects/<int:pk>/', ProjectDetail.as_view(), name='project-detail'),

    # URL patterns for tasks
    path('tasks/', TaskListCreate.as_view(), name='task-list-create'),
    path('tasks/<int:pk>/', TaskDetail.as_view(), name='task-detail'),

    # URL patterns for task assignments
    path('taskassignments/', TaskAssignmentListCreate.as_view(), name='taskassignment-list-create'),
    path('taskassignments/<int:pk>/', TaskAssignmentDetail.as_view(), name='taskassignment-detail'),

    # URL patterns for comments
    path('comments/', CommentListCreate.as_view(), name='comment-list-create'),
    path('comments/<int:pk>/', CommentDetail.as_view(), name='comment-detail'),
]
