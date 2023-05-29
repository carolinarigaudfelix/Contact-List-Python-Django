# Create your models here.
from django.db import models
from phonenumber_field.modelfields import PhoneNumberField



CATEGORY_CHOICES = (
    ('family', 'Family'),
    ('friend', 'Friend'),
    ('work', 'Work'),
    ('unknow', 'Unknow'),
)

class Contact(models.Model):
    image = models.ImageField(upload_to='images/')
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=254, verbose_name='E-mail')
    phone = PhoneNumberField()
    category = models.CharField(max_length=10, choices=CATEGORY_CHOICES, default='family')

    def get_image_url(self):
        if self.image:
            return self.image.url
        else:
            return None
        
    def __str__(self):
        return self.name
    
    

