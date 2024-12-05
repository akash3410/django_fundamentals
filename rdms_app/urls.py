from django.urls import path
from .import views

urlpatterns = [
    path('home/', views.home_page, name="home_page"),
    path('user/<int:user_id>/', views.view_by_userId, name="view_by_userId"),
]