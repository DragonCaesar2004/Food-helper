from django.urls import path
from main import views
# from .views import PasswordResetView
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('new_chat/', views.new_chat, name='new_chat'),
]