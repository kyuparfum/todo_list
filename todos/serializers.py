from rest_framework import serializers
from todos.models import TodoList


class TodoListSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = "__all__"

    def create(self, validated_data):
        user = super().create(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user

    def update(self, validated_data):
        user = super().update(validated_data)
        password = user.password
        user.set_password(password)
        user.save()
        return user


class TodoListCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoList
        fields = ("title",)
