from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from . import views

app_name = 'fms_app'

urlpatterns = [
                  path('fms_admin/', views.home, name='homepage'),
                  path('upload/', views.upload, name='uplaodpage'),
                  path('', views.student_login, name="loginpage"),
                  path('fms_student/', views.student, name='studentdashboard')
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
