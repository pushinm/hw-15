# Generated by Django 4.1.5 on 2023-01-29 21:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0006_rename_groupe_student_group'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='student',
            name='class_day',
        ),
    ]
