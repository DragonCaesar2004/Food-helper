from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('users.urls')),
    path('', include('main.urls', namespace='main')),
    #path('askgpt/', include('askgpt.urls')), 
    #path('profile/', include('userProfile.urls', namespace='userProfile')),
]
