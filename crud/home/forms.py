from django import forms
from .models import Books


#creating a form

class BookForm(forms.ModelForm):

    class Meta:
        model= Books

        fields=[
            "sno",
            "title",
            "author",
            "publisher",
            "stock",
        ]