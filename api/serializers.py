from rest_framework import serializers
from django.contrib.auth.models import User

from .models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username", "email", "first_name", "last_name"]


class CourseSerializer(serializers.ModelSerializer):
    teacher = UserSerializer(read_only=True)

    class Meta:
        model = Course
        fields = "__all__"


class StudentReadSerializer(serializers.ModelSerializer):
    course_enrolled = CourseSerializer()

    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student
        fields = "__all__"
        read_only_fields = ("id", "created_at", "updated_at")


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
        read_only_fields = ("id",)


class TimeTableReadSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = TimeTable
        fields = "__all__"
        read_only_fields = ("id",)


class TimeTableSerializer(serializers.ModelSerializer):
    class Meta:
        model = TimeTable
        fields = "__all__"
        read_only_fields = ("id",)


class SessionsReadSerializer(serializers.ModelSerializer):
    course = CourseSerializer()

    class Meta:
        model = Sessions
        fields = "__all__"
        read_only_fields = ("id",)


class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sessions
        fields = "__all__"
        read_only_fields = ("id",)


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Attendance
        fields = "__all__"
        read_only_fields = ("id",)


class AttendanceReadSerializer(serializers.ModelSerializer):
    session = SessionsReadSerializer()
    student = StudentReadSerializer()

    class Meta:
        model = Attendance
        fields = "__all__"
        read_only_fields = ("id",)


# class AttendanceBulkSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Attendance
#         fields = "__all__"
#         read_only_fields = ("id",)
    
    