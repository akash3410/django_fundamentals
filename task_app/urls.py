from django.urls import path
from .import views

urlpatterns = [
    path('tasks/', views.task_list, name="task_list"),
    path('tasks/<int:pk>', views.task_details, name="task_details")
]