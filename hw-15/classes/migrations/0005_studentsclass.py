# Generated by Django 4.1.5 on 2023-01-26 18:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('classes', '0004_alter_classwithteacher_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='StudentsClass',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Название предмета')),
            ],
            options={
                'verbose_name': 'Занятие',
                'verbose_name_plural': 'Занятия',
                'abstract': False,
            },
        ),
    ]
