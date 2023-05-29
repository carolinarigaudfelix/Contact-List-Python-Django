from django import forms
from .models import Contact



CATEGORY_CHOICES = (
    ('FAMILY', 'Family'),
    ('FRIEND', 'Friend'),
    ('WORK', 'Work'),
    ('UNKNOWN', 'Unknown'),
)

class MyForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['image', 'name', 'email', 'phone', 'category']

        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Enter name'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Enter e-mail'}), 
            'phone': forms.TextInput(attrs={'placeholder': 'Ex: +5521900000000'}),
            'category': forms.Select(choices=CATEGORY_CHOICES, attrs={'class': 'form-select'})
        }

