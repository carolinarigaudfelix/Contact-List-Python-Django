from django import forms
from .models import Contact



CATEGORY_CHOICES = (
    ('family', 'Family'),
    ('friend', 'Friend'),
    ('work', 'Work'),
    ('unknown', 'Unknown'),
)

class MyForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['image', 'name', 'email', 'phone', 'category']



