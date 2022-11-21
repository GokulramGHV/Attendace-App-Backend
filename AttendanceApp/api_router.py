from api.views import *
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("course", CourseViewSet, "course")
router.register("student", StudentViewSet, "student")
router.register("timetable", TimeTableViewSet, "timetable")
router.register("sessions", SessionsViewSet, "sessions")
router.register("attendance", AttendanceViewSet, "attendance")
app_name = "api"

urlpatterns = [
    path(r"", include(router.urls)),
    path("course/<int:pk>/students/", CourseStudentView.as_view()),
    path("course/<int:pk>/sessions/", CourseSessionsView.as_view()),
    path("attendance/session/<int:pk>/", SessionAttendanceView.as_view()),
]
