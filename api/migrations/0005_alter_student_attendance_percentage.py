# Generated by Django 4.1.3 on 2022-11-21 22:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0004_remove_attendance_course_remove_sessions_teacher_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="student",
            name="attendance_percentage",
            field=models.DecimalField(decimal_places=6, default=0.0, max_digits=7),
        ),
    ]