from django.contrib import admin
from .models import Contact

class ContactAdmin(admin.ModelAdmin):
    list_display = ('id','name','phone')

admin.site.register(Contact,ContactAdmin)
