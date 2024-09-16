from django.urls import path, include
from user_app.api.views import RegisterView, UserListView, UserDetailView
from rest_framework.authtoken.views import obtain_auth_token
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView 

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    # path('login/', obtain_auth_token, name='login'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', UserListView.as_view(), name='user_list'),
    path('<int:pk>/', UserDetailView.as_view(), name='user_detail'),
]