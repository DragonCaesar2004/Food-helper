from django.urls import path
from main import views
import users
from django.urls import path, include
# from .views import PasswordResetView
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/', views.profile, name='profile'),
    path('new_chat/', views.new_chat, name='new_chat'),
    path('error-handler/', views.error_handler, name='error_handler'),
    # path('profile/', include('users.urls')),
]