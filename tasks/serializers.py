from rest_framework import serializers
from .models import Task

class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        fields = ['id', 'title', 'email', 'description', 'created_at']

    def validate_title(self, value):
        if not value:
            raise serializers.ValidationError("El título es obligatorio.")
        return value

    def validate_email(self, value):
        if not value:
            raise serializers.ValidationError("El email es obligatorio.")
        return value
