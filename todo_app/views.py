from django.shortcuts import render
from .models import Products

# Create your views here.
def load_product(request):
    products = Products.objects.all()
    
    search_term = request.GET.get("queary")
    search_product = []
    
    
    completed = request.GET.get("completed")
    if completed == '1':
        products = products.filter(completed = True)
    elif completed == '0':
        products = products.filter(completed = False)
        
    for product in products:
        if search_term and search_term.lower() in product.title.lower():
            search_product.append(product)
            
    if search_term:
        context = {
            "products": search_product
        }
    else:
         context = {
            "products": products
        }
        
        
    return render(request, "loadproducts.html", context=context)

def product_details(request, pk):
    product = Products.objects.get(pk=pk)
    return render(request, "product_details.html", {"product": product})