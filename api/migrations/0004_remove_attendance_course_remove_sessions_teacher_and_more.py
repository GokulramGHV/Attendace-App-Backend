# Generated by Django 4.1.2 on 2022-10-08 13:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("api", "0003_alter_student_attendance_percentage"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="attendance",
            name="course",
        ),
        migrations.RemoveField(
            model_name="sessions",
            name="teacher",
        ),
        migrations.RemoveField(
            model_name="timetable",
            name="teacher",
        ),
        migrations.AlterField(
            model_name="attendance",
            name="session",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="api.sessions"
            ),
        ),
    ]
