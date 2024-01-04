from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'fms_app'

urlpatterns = [
                  path('admin/', views.admin, name='admindashboard'),
                  path('upload/', views.upload, name='uplaodpage'),
                  path('student/', views.student, name='studentdashboard')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
