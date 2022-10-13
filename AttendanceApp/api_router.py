from api.views import *
from django.urls import include, path
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("course", CourseViewSet, "course")
router.register("student", StudentViewSet, "student")
router.register("timetable", TimeTableViewSet, "timetable")
router.register("sessions", SessionsViewSet, "sessions")

app_name = "api"

urlpatterns = [
    path(r"", include(router.urls)),
]
