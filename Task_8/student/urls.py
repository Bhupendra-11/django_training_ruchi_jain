from django.urls import path
from .views import * 

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('stud/', stud, name='stud'),
    path('login/', login, name='login'),
    path('login_valid/', login_valid, name='login_valid'),
    path('home/', home, name='home'),
    path('result/',result,name='result'),
]