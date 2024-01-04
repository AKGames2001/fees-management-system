from django.urls import path
from . import views

app_name = 'fms_app'

urlpatterns = [
                  path('', views.home, name='homepage'),
                  path('login_student/', views.login_student, name='loginstudent'),
                  path('login_admin/', views.login_admin, name='loginadmin')
              ]
