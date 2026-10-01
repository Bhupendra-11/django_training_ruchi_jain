from django.urls import path
from .views import * 

urlpatterns = [
    path('logout', logout, name='logout'),
    path('signup/', signup, name='signup'),
    path('saveuser/', saveuser, name='saveuser'),
    path('login/', login, name='login'),
    path('login_valid/', login_valid, name='login_valid'),
    path('home/', home, name='home'),
]