from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# from django.utils import timezone

DAYS_OF_WEEK = (
    (0, "Monday"),
    (1, "Tuesday"),
    (2, "Wednesday"),
    (3, "Thursday"),
    (4, "Friday"),
    (5, "Saturday"),
    (6, "Sunday"),
)


class Course(models.Model):
    name = models.CharField(max_length=150)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    block_hours = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.name}"


class Student(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=100)
    reg_no = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    attendance_percentage = models.DecimalField(
        max_digits=7, decimal_places=6, default=0.00
    )
    course_enrolled = models.ForeignKey(Course, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.name}"


class Sessions(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    session = models.DateTimeField()
    block_hours = models.IntegerField(default=1)
    # teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)


class Attendance(models.Model):
    session = models.ForeignKey(Sessions, on_delete=models.CASCADE)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    # course = models.ForeignKey(Course, on_delete=models.CASCADE)


class TimeTable(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    day = models.CharField(max_length=1, choices=DAYS_OF_WEEK)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    # teacher = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
