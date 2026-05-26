from rest_framework import serializers
from user.models import User


# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
# MODEL: log-in user
# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
class LoginSerializer(serializers.Serializer):
    email = serializers.EmailField(required=False, allow_blank=True)
    mobile = serializers.CharField(max_length=11, required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        email = data.get('email', '')
        mobile = data.get('mobile', '')
        password = data['password']
        if not email and not mobile:
            raise serializers.ValidationError({"error": "email or mobile required"})

        user_field = 'email' if email else 'mobile'
        value = email or mobile

        try:
            user = User.objects.get(**{user_field: value})
        except User.DoesNotExist:
            raise serializers.ValidationError({"error": f"user this {user_field} not found."})

        if not user.check_password(password):
            raise serializers.ValidationError({"error": "Invalid  password."})

        if not user.is_verified:
            raise serializers.ValidationError({"error": "User account is not verify."})

        data['user'] = user
        return data