
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.contact_list, name='contact_list'),
    path('<int:id_contact>', views.show_contact, name = 'show_contact'),
    path('edit/<int:id_contact>', views.edit_contact, name = 'edit_contact'),
    path('new/', views.new_contact, name = 'new_contact'),
    path('delete/<int:id_contact>', views.delete_contact, name='delete_contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
