from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from django.core.mail import send_mail
from django.http import JsonResponse 
from django.contrib.auth import get_user_model 
from rest_framework import generics, status
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework_simplejwt.tokens import RefreshToken
from .models import CustomUser, Meal, Food
from .serializers import  RegisterSerializer, UserSerializer, PasswordResetSerializer, MealSerializer, FoodSerializer
import g4f
from g4f.client import Client
from g4f.Provider import RetryProvider, Phind, FreeChatgpt, Liaobots, Blackbox
import random
import string  
import json

class RegisterView(generics.CreateAPIView):
    queryset = CustomUser.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterSerializer
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
    
class ProfileView(generics.RetrieveUpdateAPIView):
    queryset = CustomUser.objects.all()
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]
    def get_object(self):
        return self.request.user

class CustomTokenObtainPairView(TokenObtainPairView):
    serializer_class = TokenObtainPairView.serializer_class
    def post(self, request, *args, **kwargs):
        response = super().post(request, *args, **kwargs)
        response.data['user'] = UserSerializer(request.user).data
        return response

class LogoutView(APIView):
    permission_classes = (IsAuthenticated,)
    def post(self, request):
        try:
            refresh_token = request.data["refresh"]
            token = RefreshToken(refresh_token)
            token.blacklist()
            return Response(status=status.HTTP_205_RESET_CONTENT)
        except Exception as e:
            return Response(status=status.HTTP_400_BAD_REQUEST)
        
def index(request):
    return render(request, 'index.html')


# @csrf_exempt
class PasswordResetAPIView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        serializer = PasswordResetSerializer(data=request.data)
        if serializer.is_valid():
            email = serializer.validated_data['mail_for_recovery']
            User = get_user_model()
            try:
                user = User.objects.get(email=email)
                new_password = ''.join(random.choices(string.ascii_letters + string.digits, k=8))
                user.set_password(new_password)
                user.save()
                print(email)
                send_mail(
                    'Ваш новый пароль',
                    f'Вы сбросили пароль на сайте Food Helper,\n вот новый пароль: {new_password} \n \n С уважением, команда Food Helper',
                    'foodhelperproject@gmail.com',
                    [email],
                    fail_silently=False,
                )
                return Response({'message': 'A new password has been sent to your email.'}, status=status.HTTP_200_OK)
            except User.DoesNotExist:
                return Response({'error': 'Email not registered in the system.'}, status=status.HTTP_404_NOT_FOUND)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class UpdateProfileView(APIView):
    permission_classes = [IsAuthenticated]
    def put(self, request):
        user = request.user
        data = request.data
        user.email = data.get('email', user.email)
        user.date_of_birth = data.get('date_of_birth', user.date_of_birth)
        user.goal = data.get('goal', user.goal)
        user.gender = data.get('gender', user.gender)
        user.vegan_vegetarian = data.get('vegan_vegetarian', user.vegan_vegetarian)
        user.allergies = data.get('allergies', user.allergies)
        user.weight = data.get('weight', user.weight)
        user.height = data.get('height', user.height)
        user.save()
        serializer = UserSerializer(user)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
class UserMealsView(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request, *args, **kwargs):
        user = request.user
        print('hello')
        meals = Meal.objects.filter(user_id=user.id)
        serializer = MealSerializer(meals, many=True)
        return Response(serializer.data)

class MealCreateView(generics.CreateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]
    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class FoodCreateView(generics.CreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
    
@csrf_exempt
def generate_description(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        food_name = data.get('food_name')
        quantity = data.get('quantity')
        mealType = data.get('mealType')
        food_type = data.get('food_type')
        prompt = data.get('prompt')
        client = Client(provider=RetryProvider([Blackbox], shuffle=False))
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"{prompt}. Сегодня на {mealType} я поел {food_name}. Количество: {quantity} {food_type}. Исходя из этих данных кратко скажи расскажи про мой прием: сколько калории, что я получил, как это вляет на мой организм, и полезно ли для моих данных. Не используй жирный и курсивный шрифты и формулы!"}],
            )
            description = response.choices[0].message.content
            return JsonResponse({'description': description[13:]}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def generate_description2(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        food_name = data.get('food_name')
        quantity = data.get('quantity')
        mealType = data.get('mealType')
        food_type = data.get('food_type')
        prompt = data.get('prompt')
        client = Client(provider=RetryProvider([Blackbox], shuffle=False))
        try:
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": f"{prompt}. Сегодня на {mealType} я поел {food_name}. Количество: {quantity} {food_type}. Проанализируй данные и дай оценку в видее только одной цифры от 0 до 10. Мне нужно только одно число без текста!"}],
            )
            description = response.choices[0].message.content
            description += "/10"
            return JsonResponse({'description': description[13:]}, status=200)
        except Exception as e:
            return JsonResponse({'error': str(e)}, status=500)
    else:
        return JsonResponse({'error': 'Invalid request method'}, status=400)

class UserMealsView(generics.ListAPIView):
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        return Meal.objects.filter(user=self.request.user)

class MealDeleteView(generics.DestroyAPIView):
    queryset = Meal.objects.all()
    permission_classes = [IsAuthenticated]
    def delete(self, request, *args, **kwargs):
        meal_id = kwargs.get('pk')
        meal = self.get_queryset().filter(id=meal_id, user=request.user).first()
        if meal:
            meal.delete()
            return Response(status=status.HTTP_204_NO_CONTENT)
        return Response(status=status.HTTP_404_NOT_FOUND)

class FoodListView(generics.ListCreateAPIView):
    queryset = Food.objects.all()
    serializer_class = FoodSerializer
    permission_classes = [IsAuthenticated]
    def get_queryset(self):
        user = self.request.user
        return Food.objects.filter(meal__user=user)
    def perform_create(self, serializer):
        serializer.save()

class MealUpdateView(generics.UpdateAPIView):
    queryset = Meal.objects.all()
    serializer_class = MealSerializer
    permission_classes = [IsAuthenticated]
    def patch(self, request, *args, **kwargs):
        meal_id = kwargs.get('pk')
        meal = self.get_queryset().filter(id=meal_id, user=request.user).first()
        if not meal:
            return Response({'error': 'Meal not found or not authorized'}, status=status.HTTP_404_NOT_FOUND)
        mark = request.data.get('mark')
        if mark:
            meal.mark = mark
            meal.save()
            return Response({'message': 'Meal type updated successfully'}, status=status.HTTP_200_OK)
        return Response({'error': 'Meal type not provided'}, status=status.HTTP_400_BAD_REQUEST)