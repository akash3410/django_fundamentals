from django.urls import path
from .import views

urlpatterns = [
    path('', views.initial_load),
    path('home/', views.home_page),
    path('home/<username>', views.home_page),
    path('about/', views.about),
    path('work/', views.work),
    path('images/', views.images)
]