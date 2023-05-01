from django.contrib import admin
from django.urls import path, include
from contacts import views as contact_views


urlpatterns = [
    path('', include('contacts.urls')),
    path('admin/', admin.site.urls),
]