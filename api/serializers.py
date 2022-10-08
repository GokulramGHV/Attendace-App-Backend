from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name']

class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    class Meta:
        model = Course
        fields = ['id', 'name', 'created_at', 'updated_at', 'teacher']

class StudentSerializer(serializers.ModelSerializer):
    course_enrolled = CourseSerializer(read_only=True)
    class Meta:
        model = Student
        fields = ['id', 'name', 'email', 'reg_no', 'attendance_percentage', 'course_enrolled', 'created_at', 'updated_at']

class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = ['session', 'student', 'course']

class TimeTableSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)
    class Meta:
        model = TimeTable
        fields = ['start_time', 'end_time', 'day', 'course', 'teacher']

class SessionsSerializer(serializers.ModelSerializer):
    course = CourseSerializer(read_only=True)
    teacher = UserSerializer(read_only=True)
    class Meta:
        model = Sessions
        fields = ['course', 'teacher', 'session']