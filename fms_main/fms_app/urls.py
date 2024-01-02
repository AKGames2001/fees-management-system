from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'fms_app'

urlpatterns = [
    path('', views.home, name='homepage'),
    path('upload/', views.upload, name='uplaodpage')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)