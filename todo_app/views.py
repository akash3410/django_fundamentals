from django.shortcuts import render, redirect
from .models import Products
from .forms import SearchProduct, AddProduct

# Create your views here.
def load_product(request):
    products = Products.objects.all()
    
    # Get search item from forms
    search_forms = SearchProduct(request.GET)
    search_term = ""
    
    if search_forms.is_valid():
        search_term = search_forms.cleaned_data.get("title")
     
    # search_term = request.GET.get("queary")
    
    # Search Product
    search_product = []
    for product in products:
        if search_term and search_term.lower() in product.title.lower():
            search_product.append(product)
            
    
    # Completed an Incompleted Task
    completed = request.GET.get("completed")
    if completed == '1':
        products = products.filter(completed = True)
    elif completed == '0':
        products = products.filter(completed = False)
    
    # Context difference   
    if search_term:
        context = {
            "products": search_product,
            "forms": search_forms,
        }
    else:
         context = {
            "products": products,
            "forms": search_forms,
        }
        
        
    return render(request, "loadproducts.html", context=context)

def product_details(request, pk):
    product = Products.objects.get(pk=pk)
    return render(request, "product_details.html", {"product": product})

def add_product(request):
    if request.method =="POST":
        add_form = AddProduct(request.POST)
        if add_form.is_valid():
            add_form.save()
            return redirect("load_product")
        
    add_form = AddProduct()
    return render(request, "addproduct.html", {"forms": add_form})
    
    