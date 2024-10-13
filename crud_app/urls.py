from django.urls import path
from .import views

urlpatterns = [
    path('items/', views.all_items, name="all_items"),
    path('items/<int:pk>', views.item_details, name="item_details"),
    path('static/add/', views.add_static_item, name="add_static_item"),
    path('delete/<int:pk>', views.delete_item, name="delete_item"),
    path('static/update/<int:pk>', views.staic_update_item, name="staic_update_item"),
    path('update/<int:pk>', views.update_item, name="update_item"),
    path('add/', views.add_item, name="add_item"),
]