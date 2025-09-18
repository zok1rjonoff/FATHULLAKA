from rest_framework import serializers
from .models import Users


class UsersSerializer(serializers.ModelSerializer):
    class Meta:
        model = Users
        fields = [
            "id",
            "username",
            "first_name",
            "last_name",
            "email",
            "phone_number",
            "password",
        ]
        extra_kwargs = {
            "password": {"write_only": True},   # password API orqali qaytmasin
            "first_name": {"required": True},   # majburiy
            "last_name": {"required": True},    # majburiy
        }

    def create(self, validated_data):
        password = validated_data.pop("password")  # parolni olish
        user = Users(**validated_data)
        user.set_password(password)                # parolni hash qilish
        user.save()
        return user

    def update(self, instance, validated_data):
        password = validated_data.pop("password", None)

        for attr, value in validated_data.items():
            setattr(instance, attr, value)

        if password:
            instance.set_password(password)

        instance.save()
        return instance
