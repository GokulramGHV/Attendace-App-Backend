from pyexpat import model
from statistics import mode
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from api.serializers import *
from api.models import *
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import generics, status

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

    def get_serializer_class(
        self,
    ):  # refer https://stackoverflow.com/questions/41312558/django-rest-framework-post-nested-objects
        if self.request.method in ["GET"]:
            return StudentReadSerializer
        return StudentSerializer


class CourseStudentView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        students = Student.objects.filter(course_enrolled_id=pk)
        print(len(students))
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data)


class TimeTableViewSet(ModelViewSet):
    queryset = TimeTable.objects.all()
    serializer_class = TimeTableSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return TimeTable.objects.filter(course__teacher=self.request.user)

    def get_serializer_class(
        self,
    ):  # refer https://stackoverflow.com/questions/41312558/django-rest-framework-post-nested-objects
        if self.request.method in ["GET"]:
            return TimeTableReadSerializer
        return TimeTableSerializer


class SessionsViewSet(ModelViewSet):
    queryset = Sessions.objects.all()
    serializer_class = SessionsSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Sessions.objects.filter(course__teacher=self.request.user)

    def get_serializer_class(
        self,
    ):  # refer https://stackoverflow.com/questions/41312558/django-rest-framework-post-nested-objects
        if self.request.method in ["GET"]:
            return SessionsReadSerializer
        return SessionsSerializer


class CourseSessionsView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        sessions = Sessions.objects.filter(course_id=pk)
        serializer = SessionsReadSerializer(sessions, many=True)
        return Response(serializer.data)


class AttendanceViewSet(ModelViewSet):
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer
    permission_classes = (IsAuthenticated,)

    def get_queryset(self):
        return Attendance.objects.filter(session__course__teacher=self.request.user)

    def get_serializer_class(
        self,
    ):
        if self.request.method in ["GET"]:
            return AttendanceReadSerializer
        return AttendanceSerializer


class SessionAttendanceView(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request, pk, format=None):
        attendance = Attendance.objects.filter(session_id=pk)
        serializer = AttendanceReadSerializer(attendance, many=True)
        return Response(serializer.data)


class BulkAttendanceView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Attendance.objects.all()
    serializer_class = AttendanceSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, many=True)
        student_data = request.data
        student_ids = []
        for student in student_data:
            student_ids.append(student["student"])
        all_students = Student.objects.filter(
            course_enrolled__teacher=self.request.user
        )
        for student in all_students:
            percent = student.attendance_percentage
            total_sessions = (
                len(Sessions.objects.filter(course__teacher=self.request.user)) - 1
            )
            # if total_sessions != 0:
            attended_sessions = total_sessions * percent
            if student.id not in student_ids:
                attended_sessions += 1
            student.attendance_percentage = attended_sessions / (total_sessions + 1)
            student.save()

        serializer.is_valid(raise_exception=True)
        try:
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
