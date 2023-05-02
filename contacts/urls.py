
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.list),
    path('<int:id_contact>', views.show_contact, name = 'show_contact'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
