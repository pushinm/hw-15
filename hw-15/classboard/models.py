from django.db import models

import classes.models
# from teachers.models import Teacher
from classes.models import Class, ClassPairChoices, ClassByDayChoices

# Create your models here.

class Classboard(models.Model):
    class_day = models.CharField(verbose_name='День недели', max_length=6, choices=ClassByDayChoices.choices,
                                  default=ClassByDayChoices.MO)
    class_pair = models.CharField(verbose_name='Пара', max_length=6, choices=ClassPairChoices.choices,
                                  default=ClassPairChoices.PAIR_1)
    class_name = models.ForeignKey(verbose_name='Занятие', to='classes.Class', on_delete=models.CASCADE)
    group = models.ForeignKey(verbose_name='Группа', to='students.Group', on_delete=models.CASCADE)
    teacher = models.ManyToManyField(verbose_name='Преподаватель', to='teachers.Teacher', related_name='classboard_teacher')
    class Meta:
        ordering = ['class_name', ]

        verbose_name = 'Расписание'
        verbose_name_plural = 'Расписание'

    def __str__(self) -> str:
        return f'{self.class_name}'
