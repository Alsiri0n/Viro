from django.db import models
# from customuser.models import ViroUser
# Create your models here.


class Criterion(models.Model):
    # user = models.ForeignKey(ViroUser)
    year = models.CharField(max_length=4, verbose_name='Год проведения',
                            default="2017")
    number = models.CharField(max_length=5, verbose_name='Номер', default=1)
    ages = models.CharField(max_length=40, verbose_name='Возраст детей',
                            blank=True)
    # conclusion = models.TextField(verbose_name='Выводы', blank=True)
    description = models.CharField(max_length=300, verbose_name='Описание')
    deadline = models.CharField(max_length=100,
                                verbose_name='Срок проведения', blank=True)
    goal = models.CharField(max_length=300, verbose_name='Цель', blank=True)
    # qnt = models.PositiveSmallIntegerField(
    #     verbose_name='Кол-во детей данного возраста в МОУ', default=0)
    # qntExam = models.PositiveSmallIntegerField(
    #     verbose_name='Из них обследовано', default=0)
    responsible = models.CharField(max_length=100,
                                   verbose_name='Ответственный за проведение',
                                   blank=True)
    subject = models.CharField(max_length=300,
                               verbose_name='Предмет исследования',
                               blank=True)
    tools = models.CharField(max_length=300,
                             verbose_name='Диагностический инструментарий',
                             blank=True)

    def __str__(self):
        return self.number

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'
        ordering = ('number',)
