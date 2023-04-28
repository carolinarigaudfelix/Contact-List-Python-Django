# Create your models here.
from django.db import models
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length= 50)
    
    def _str_(self):
        return self.name
    

class Contact(models.Model):
    name = models.CharField(max_length=50)
    email = models.CharField(max_length=256, null=True, blank=True)
    phone = models.CharField(max_length=256)
    photo = models.ImageField(upload_to='photos/')
    category = models.ForeignKey(Category, on_delete=models.DO_NOTHING)
    creation_date = models.DateTimeField(default=timezone.now)

    def _str_(self):
        return self.name