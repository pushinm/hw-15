# Generated by Django 4.1.5 on 2023-01-26 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0007_classbyday_delete_studentsclass'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classbyday',
            options={'verbose_name': 'Занятие + Дни недели', 'verbose_name_plural': 'Занятия + Дни недели'},
        ),
        migrations.RemoveField(
            model_name='classbyday',
            name='name',
        ),
        migrations.AddField(
            model_name='classbyday',
            name='class_name',
            field=models.ManyToManyField(to='classes.class', verbose_name='Название предмета'),
        ),
    ]
