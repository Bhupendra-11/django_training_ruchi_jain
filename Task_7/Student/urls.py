from django.urls import path
from .views import * 

urlpatterns = [
    path('signup/',signup, name='signup'),
    path('saveuser/',saveuser, name='saveuser'),
    path('login/',login, name='login'),
    path('login_valid/',login_valid, name='login_valid'),
    path('newStudentForm/',newStudentForm, name='newStudentForm'),
    path('home/',home, name='home'),
    path('saveStudent/',saveStudent, name='saveStudent'),
    path('studentlist', studentlist, name='studentlist'),
]