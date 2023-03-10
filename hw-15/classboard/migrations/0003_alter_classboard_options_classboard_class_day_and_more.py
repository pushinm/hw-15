# Generated by Django 4.1.5 on 2023-01-28 15:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('teachers', '0010_remove_teacher_to_class'),
        ('students', '0004_student_class_day'),
        ('classes', '0015_delete_classroom'),
        ('classboard', '0002_alter_classboard_options'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='classboard',
            options={'ordering': ['class_name'], 'verbose_name': 'Расписание', 'verbose_name_plural': 'Расписание'},
        ),
        migrations.AddField(
            model_name='classboard',
            name='class_day',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='classes.classbyday', verbose_name='День недели'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='classboard',
            name='class_pair',
            field=models.CharField(choices=[('1', 'Первая пара'), ('2', 'Вторая пара'), ('3', 'Третья пара'), ('4', 'Четвертая пара'), ('5', 'Пятая пара'), ('6', 'Шестая пара'), ('7', 'Седьмая пара'), ('8', 'Восьмая пара')], default='1', max_length=6, verbose_name='Пара'),
        ),
        migrations.AddField(
            model_name='classboard',
            name='group',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='students.group', verbose_name='Группа'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='classboard',
            name='class_name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='classes.class', verbose_name='Занятие'),
        ),
        migrations.RemoveField(
            model_name='classboard',
            name='teacher',
        ),
        migrations.AddField(
            model_name='classboard',
            name='teacher',
            field=models.ManyToManyField(to='teachers.teacher', verbose_name='Преподаватель'),
        ),
    ]
