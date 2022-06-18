
from unicodedata import name
from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from Api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/',include('Api.url')),
    path('', Login_funk,name = 'login'),
    path('adminlar/', Admin_Page,name = 'admin'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
