from django.contrib.auth import get_user_model
from rest_framework import serializers


# Get the User Model
User = get_user_model()


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True, required=True)
    # confirm_password = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = User
        fields = [
            'id', 'email', 'username', 'date_joined',
            'first_name', 'last_name',
            'password',
        ]
        read_only_fields = ('date_joined',)

    def create(self, validated_data):
        return User.objects.create_user(**validated_data)
