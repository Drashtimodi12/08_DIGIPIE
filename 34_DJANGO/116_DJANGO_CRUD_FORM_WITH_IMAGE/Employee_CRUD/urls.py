from django.urls import path
from Employee_CRUD.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', form, name='form'),
    path('register/', registerEmp, name='register'),
    path('update/', updateEmp, name='update'),
    path('delete/', deleteEmp, name='delete')
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
