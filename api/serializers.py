from rest_framework import serializers

from .models import *

class CourseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Course
        fields = ['id', 'name', 'created_at', 'updated_at', 'teacher']