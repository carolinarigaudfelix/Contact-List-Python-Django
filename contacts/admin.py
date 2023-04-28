from django.contrib import admin
from .models import Category, Contact

class ContatoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone', 'email',
                    'category', 'creation_date')

admin.site.register(Contact)
admin.site.register(Category)
