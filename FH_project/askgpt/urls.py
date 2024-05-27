from django.urls import path
from . import views


urlpatterns = [
    path('', views.home, name='home'),
    path('new-chat/', views.new_chat, name='new_chat'),
    path('error-handler/', views.error_handler, name='error_handler'),
]

