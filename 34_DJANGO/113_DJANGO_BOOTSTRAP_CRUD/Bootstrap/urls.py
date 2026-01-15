from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from Bootstrap.views import *

urlpatterns = [
    path('', form, name='form'),
    path('register', register, name='register'),
    path('delete', delete, name='delete'),
    path('edit', edit, name='edit'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)