from django.urls import path
from .views import RegisterView, ProfileView, LogoutView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MealCreateView, UpdateProfileView
# from django.contrib.auth.views import PasswordResetView
from .views import PasswordResetAPIView
from . import views
# from .views import PasswordResetView
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recovery-password/', PasswordResetAPIView.as_view(), name='recovery-password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('meal/', MealCreateView.as_view(), name='meal_create'), 
]
