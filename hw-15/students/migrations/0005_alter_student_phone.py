# Generated by Django 4.1.5 on 2023-01-28 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0004_student_class_day'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='phone',
            field=models.CharField(max_length=14, verbose_name='Телефон'),
        ),
    ]
