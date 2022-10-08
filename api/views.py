from pyexpat import model
from statistics import mode
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import *
from api.models import *
from rest_framework.permissions import IsAuthenticated
# from api.authentication import TokenAuthentication

# Create your views here.


class CourseViewSet(ModelViewSet):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Course.objects.filter(teacher=self.request.user)

    def perform_create(self, serializer):
        serializer.save(teacher=self.request.user)


class StudentViewSet(ModelViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Student.objects.filter(course_enrolled__teacher=self.request.user)

class TimeTableViewSet(ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TimeTable.objects.filter(teacher=self.request.user)

