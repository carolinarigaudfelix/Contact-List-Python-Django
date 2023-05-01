
from django.urls import path
from . import views

urlpatterns = [
    path('', views.list),
    path('<int:contact_id>', views.show_contact, name = 'show_contact'),
]
