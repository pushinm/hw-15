# Generated by Django 4.1.5 on 2023-01-24 20:52

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('wages', '0005_alter_wage_year'),
    ]

    operations = [
        migrations.AddField(
            model_name='wage',
            name='month',
            field=models.DateField(auto_now_add=True, choices=[(1, 1)], default=django.utils.timezone.now, verbose_name='Месяц'),
            preserve_default=False,
        ),
    ]
