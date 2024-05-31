from rest_framework import serializers
from .models import CustomUser, Meal, Food


from rest_framework import serializers
from .models import CustomUser, Meal, Food

class FoodSerializer(serializers.ModelSerializer):
    class Meta:
        model = Food
        fields = ['id', 'meal', 'date', 'name_of_food', 'quantity', 'description']

class MealSerializer(serializers.ModelSerializer):
    foods = FoodSerializer(many=True, read_only=True, source='food_set')

    class Meta:
        model = Meal
        fields = ['id', 'meal_type', 'time', 'date', 'foods']

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'date_of_birth', 'goal', 'gender', 'vegan_vegetarian', 'allergies', 'weight', 'height']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'password', 'date_of_birth', 'goal', 'gender', 'vegan_vegetarian', 'allergies', 'weight', 'height']

    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            password=validated_data['password'],
            date_of_birth=validated_data['date_of_birth'],
            goal=validated_data['goal'],
            gender=validated_data['gender'],
            vegan_vegetarian=validated_data['vegan_vegetarian'],
            allergies=validated_data['allergies'],
            weight=validated_data['weight'],
            height=validated_data['height']
        )
        return user

class PasswordResetSerializer(serializers.Serializer):
    mail_for_recovery = serializers.EmailField()


