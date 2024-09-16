from django.shortcuts import render
from .models import Products

# Create your views here.
def load_product(request):
    products = Products.objects.all()
    completed = request.GET.get("completed")
    if completed == '1':
        products = products.filter(completed = True)
    elif completed == '0':
        products = products.filter(completed = False)
        
    return render(request, "loadproducts.html", {"products": products})

def product_details(request, pk):
    product = Products.objects.get(pk=pk)
    return render(request, "product_details.html", {"product": product})