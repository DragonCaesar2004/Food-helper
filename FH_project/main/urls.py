from django.urls import path
from main import views
# from .views import PasswordResetView
app_name = 'main'

urlpatterns = [
    path('', views.index, name='index'),
    # path('password-reset/', PasswordResetView.as_view(), name='password-reset'),

    
]

