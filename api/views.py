from pyexpat import model
from statistics import mode
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import *
from api.models import *
from rest_framework.permissions import IsAuthenticated

# from rest_framework.authentication import SessionAuthentication
from api.authentication import TokenAuthentication

# Create your views here.
# from rest_framework.authentication import TokenAuthentication
# from dj_rest_auth.registration.views import LoginView


# class LoginViewCustom(LoginView):
#     authentication_classes = (TokenAuthentication,)


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

    def get_serializer_class(self):     # refer https://stackoverflow.com/questions/41312558/django-rest-framework-post-nested-objects
        if self.request.method in ['GET']:
            return StudentReadSerializer
        return StudentSerializer
class TimeTableViewSet(ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TimeTable.objects.filter(course__teacher=self.request.user)


class SessionsViewSet(ModelViewSet):
    queryset = Sessions.objects.all()
    serializer_class = SessionsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Sessions.objects.filter(course__teacher=self.request.user)

    def get_serializer_class(self):     # refer https://stackoverflow.com/questions/41312558/django-rest-framework-post-nested-objects
        if self.request.method in ['GET']:
            return SessionsReadSerializer
        return SessionsSerializer
