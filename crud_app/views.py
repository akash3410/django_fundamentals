from django.shortcuts import render, redirect
from .models import Items
from .forms import AddForm, UpdateForm, SearchForm

# Create your views here.
def all_items(request):
    items = Items.objects.all()
    if request.method == "POST":
        forms = SearchForm(request.POST)
        if forms.is_valid():
            search_term = forms.cleaned_data.get("title")
            search_items = items.filter(title__icontains = search_term)
            if search_items:
                return render(request, 'items.html', {"items": search_items, "forms":forms})
            else:
                return render(request, 'items.html', {"message": "No Items Found!", "forms":forms, "items": items})  
    else:
        forms = SearchForm()
        return render(request, 'items.html', {"items": items, "forms": forms})

def item_details(request, pk):
    try:
        item = Items.objects.get(pk=pk)
        return render(request, 'item_details.html', {"item": item})
    except Items.DoesNotExist:
        return redirect("all_items")
    
def add_static_item(request):
    _title = "Ice-cream"
    _description = "This is vanila flavure Ice-Cream."
    _completed = False
    _due_date = "2024-10-18"
    _updated_by = "Fuzi"
    
    item = Items(title = _title, description = _description, completed = _completed, due_date = _due_date, updated_by = _updated_by)
    item.save()
    return redirect("all_items")

def delete_item(request, pk):
    try:
        item = Items.objects.get(pk=pk)
        item.delete()
        return redirect("all_items")
    except Items.DoesNotExist:
        return redirect("all_items")
    
def staic_update_item(request, pk):
    try:
        item = Items.objects.get(pk=pk)
        item.title ="Updated " + item.title
        item.save()
        return redirect("all_items")
    except Items.DoesNotExist:
        return redirect("all_items")

def add_item(request):
    if request.method == 'POST':
        form = AddForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('all_items')
        else:
            return render(request, 'add_form.html', {"form": form})
    else:
        form = AddForm()
        return render(request, 'add_form.html', {"form": form})
    
def update_item(request, pk):
    try:
        item = Items.objects.get(pk=pk)
        if request.method == "POST":
            forms = UpdateForm(request.POST, instance=item)
            if forms.is_valid():
                forms.save()
                return redirect("all_items")
            else:
                return render(request, 'update.html', {"forms": forms})
        forms = UpdateForm(instance=item)
        return render(request, 'update.html', {"forms": forms})
    except Items.DoesNotExist:
        return redirect("all_items")