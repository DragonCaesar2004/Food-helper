from django.urls import path
from .views import RegisterView, ProfileView, LogoutView, PasswordResetAPIView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from .views import MealCreateView, UpdateProfileView, FoodCreateView, generate_description
from . import views
 
urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('profile/', ProfileView.as_view(), name='profile'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('recovery-password/', PasswordResetAPIView.as_view(), name='recovery-password'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('update-profile/', UpdateProfileView.as_view(), name='update-profile'),
    path('meal/', MealCreateView.as_view(), name='meal_create'), 
    path('food/', FoodCreateView.as_view(), name='food-create'),
    path('generate-description/', generate_description, name='generate-description'),
]
