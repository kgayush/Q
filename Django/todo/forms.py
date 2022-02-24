from django import forms
from .models import ToDo

class MyForm(forms.ModelForm):
    class Meta:
        model = ToDo
        fields = ["title", "desc",]
        labels = {"title": "Todo Title", "desc": "Todo Description",}
    