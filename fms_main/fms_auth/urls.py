from django.urls import path
from . import views

app_name = 'fms_app'

urlpatterns = [
                  path('', views.home, name='homepage'),
                  path('login_student/', views.login_student, name='loginstudent'),
                  path('register_student/', views.register_student, name='registerstudent'),
                  path('login_admin/', views.login_admin, name='loginadmin'),
                  path('register_admin/', views.register_admin, name='registeradmin'),
              ]
