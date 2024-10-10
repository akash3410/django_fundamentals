from django import forms
from .models import Products

class SearchProduct(forms.Form):
    title = forms.CharField(label='Title', required=False)
    

class AddProduct(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['title', 'description', 'completed', 'due_date']
        # widgets = {
        #     'title': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Enter your name'})
        # }
