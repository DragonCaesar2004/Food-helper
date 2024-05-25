from rest_framework import serializers
from django.contrib.auth import get_user_model

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'date_of_birth', 'goal', 'gender', 'vegan_vegetarian', 'allergies', 'weight', 'height']

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password', 'date_of_birth', 'goal', 'gender', 'vegan_vegetarian', 'allergies', 'weight', 'height']

    def create(self, validated_data):
        user = User.objects.create_user(
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


from rest_framework import serializers

class PasswordResetSerializer(serializers.Serializer):
    mail_for_recovery = serializers.EmailField()
