from django.urls import path
from .import views
urlpatterns = [
    path('products/', views.load_product, name="load_product"),
    path('products/<int:pk>', views.product_details, name="product_details")
]
 