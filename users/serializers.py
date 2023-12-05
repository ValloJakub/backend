from rest_framework import serializers
from users.models import CustomUser

class RegistrationSerializer(serializers.ModelSerializer):
    password_confirmation = serializers.CharField(write_only=True)

    class Meta:
        model = CustomUser
        fields = ['email', 'password', 'password_confirmation', 'phone_number']

    def create(self, validated_data):
        password_confirmation = validated_data.pop('password_confirmation', None)
        if validated_data['password'] != password_confirmation:
            raise serializers.ValidationError("Passwords do not match")
        user = CustomUser.objects.create_user(**validated_data)
        return user

class LoginSerializer(serializers.Serializer):
        email = serializers.EmailField()
        password = serializers.CharField()

        def validate(self, data):
            email = data.get('email')
            password = data.get('password')

            if email and password:
                return data
            else:
                raise serializers.ValidationError('Must include "email" and "password".')

