from django import forms
from .models import Items

class AddForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            "title",
            "description",
            "completed",
            "due_date",
            "updated_by",
        ]
    #control indivisual field
    due_date = forms.DateField(widget=forms.DateInput(attrs={"type": "date"}))
    description = forms.CharField(widget=forms.TextInput())
    
class UpdateForm(forms.ModelForm):
    class Meta:
        model = Items
        fields = [
            "title",
            "description",
            "completed",
        ]
    description = forms.CharField(widget=forms.TextInput())

class SearchForm(forms.Form):
    title = forms.CharField(required=False)
    widget = {
        'title': forms.TextInput(attrs={"placeholder": "Search here..."})
    }