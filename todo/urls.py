from django.urls import path
from . import views

urlpatterns = [
    path('add_task/', views.add_task, name='add_task'),
    path('done/<int:pk>/', views.done, name='done'),
    path('undone/<int:pk>/', views.undone, name='undone'),
    path('edit/<int:pk>/', views.edit, name='edit'),
    path('delete_task/<int:pk>', views.delete_task, name='delete_task'),
]
