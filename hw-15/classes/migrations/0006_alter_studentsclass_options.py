# Generated by Django 4.1.5 on 2023-01-26 18:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0005_studentsclass'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='studentsclass',
            options={'verbose_name': 'Занятие + Студент', 'verbose_name_plural': 'Занятия + Студенты'},
        ),
    ]
