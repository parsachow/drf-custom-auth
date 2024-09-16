from django.urls import path
from .views import Login, Register, Logout, Home


urlpatterns = [
    path('home/', Home.as_view(), name='user_list'),
    path('login/', Login.as_view(), name='login'),
    path('logout/', Logout.as_view(), name='logout'),
    path('signup/', Register.as_view(), name='register')
    
]