# Create your models here.
from django.db import models




CATEGORY_CHOICES = (
    ('family', 'Family'),
    ('friend', 'Friend'),
    ('work', 'Work'),
    ('unknow', 'Unknow'),
)

class Contact(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254)
    phone = models.CharField(max_length=20)
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='family')

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return None
        
    def __str__(self):
        return self.name
    
    

