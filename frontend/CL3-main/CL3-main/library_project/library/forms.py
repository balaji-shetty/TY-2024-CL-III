from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'classification']
        widgets = {
            'classification': forms.Select(choices=Book.CLASSIFICATION_CHOICES),
        }
