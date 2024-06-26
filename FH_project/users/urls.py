from django.urls import path
from . import views
from .views import RegisterView, ProfileView, LogoutView, MealDeleteView, UserMealsView, MealUpdateView, PasswordResetAPIView, MealCreateView, UpdateProfileView, FoodCreateView, generate_description, generate_description2, FoodListView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

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
    path('generate-description2/', generate_description2, name='generate-description2'),
    path('user-meals/', UserMealsView.as_view(), name='user_meals'),
    path('meal/<int:pk>/delete/', MealDeleteView.as_view(), name='meal_delete'),
    path('food2/', FoodListView.as_view(), name='food_list'),  
    path('meal/<int:pk>/update/', MealUpdateView.as_view(), name='meal_update'),
]
