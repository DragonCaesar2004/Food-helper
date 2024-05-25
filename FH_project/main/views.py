from django.http import HttpResponse
from django.shortcuts import render
# Create your views here.

def index(request):
    return render(request, 'index.html')


# views.py
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.views import APIView
# from rest_framework.permissions import AllowAny
# from rest_framework.response import Response
# from rest_framework import status
# from django.contrib.auth.models import User
# import random
# import string
# from django.core.mail import send_mail

# @csrf_exempt  # Это отключает CSRF защиту для данного эндпоинта
# class PasswordResetAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = PasswordResetSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['mail_for_recovery']
#             try:
#                 user = User.objects.get(email=email)
#                 new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#                 user.set_password(new_password)
#                 user.save()
                
#                 # Отправка письма с новым паролем
#                 send_mail(
#                     'Password Reset',
#                     f'Your new password is: {new_password}',
#                     'from@example.com',
#                     [email],
#                     fail_silently=False,
#                 )
                
#                 return Response({'message': 'A new password has been sent to your email.'}, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({'error': 'Email not registered in the system.'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



from django.contrib.auth import get_user_model
from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework import status
from django.core.mail import send_mail
import random
import string

# Импорт вашего сериализатора
from .serializers import PasswordResetSerializer

# Представление для главной страницы
def index(request):
    return render(request, 'index.html')

# @csrf_exempt  # Это отключает CSRF защиту для данного эндпоинта
# class PasswordResetAPIView(APIView):
#     permission_classes = [AllowAny]

#     def post(self, request):
#         serializer = PasswordResetSerializer(data=request.data)
#         if serializer.is_valid():
#             email = serializer.validated_data['mail_for_recovery']
#             User = get_user_model()
            
#             try:
#                 user = User.objects.get(email=email)
                
#                 # Генерация нового пароля
#                 new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
#                 user.set_password(new_password)
#                 user.save()
                
#                 # Отправка письма с новым паролем
#                 send_mail(
#                     'Password Reset',
#                     f'Your new password is: {new_password}',
#                     'from@example.com',  # Замените на реальный адрес отправителя
#                     [email],
#                     fail_silently=False,
#                 )
                
#                 return Response({'message': 'A new password has been sent to your email.'}, status=status.HTTP_200_OK)
#             except User.DoesNotExist:
#                 return Response({'error': 'Email not registered in the system.'}, status=status.HTTP_404_NOT_FOUND)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
