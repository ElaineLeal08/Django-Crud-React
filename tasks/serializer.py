from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):
    class Meta:
        model = Task
        #fields = ('tittle', 'description', 'done')
        fields = '__all__'