from django.urls import path
from . import views

urlpatterns = [
    # Add Task Routing
    path('add_task/', views.add_task, name='add_task'),
    # Complete Task Routing
    path('done/<int:pk>/', views.done, name='done'),
    # Uncomplete Task Routing
    path('undone/<int:pk>/', views.undone, name='undone'),
    # Add Task Routing
    path('edit/<int:pk>/', views.edit, name='edit'),
    # Delete task Routing
    path('delete_task/<int:pk>/', views.delete_task, name='delete_task'),
]
