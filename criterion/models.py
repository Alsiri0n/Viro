from django.db import models

# Create your models here.


class Criterion(models.Model):
    year = models.PositiveSmallIntegerField(verbose_name='Год проведения',
                                            default=2017)
    number = models.PositiveIntegerField(verbose_name='Номер', default=1)
    ages = models.CharField(max_length=40, verbose_name='Возраст детей',
                            blank=True)
    description = models.CharField(max_length=300, verbose_name='Описание')
    deadline = models.CharField(max_length=100,
                                verbose_name='Срок проведения', blank=True)
    goal = models.CharField(max_length=300, verbose_name='Цель', blank=True)
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
        return str(self.number)

    @classmethod
    def create(cls, crit, num):
        criterion = cls(
            year=crit.year,
            number=num,
            ages=crit.ages,
            description=crit.description,
            deadline=crit.deadline,
            goal=crit.goal,
            responsible=crit.responsible,
            subject=crit.subject,
            tools=crit.tools,
        )

        return criterion

    class Meta:
        verbose_name = 'Критерий'
        verbose_name_plural = 'Критерии'
        ordering = ('number',)


class CriterionList(models.Model):
    criterion = models.ManyToManyField(Criterion)
    name = models.CharField(max_length=50, verbose_name='Район пользователя',
                            default=None)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Список критериев'
        verbose_name_plural = 'Список критериев'
