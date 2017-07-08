from django.db import models
from criterion.models import Criterion
# Create your models here.


class Answer(models.Model):
    criterion = models.ForeignKey(Criterion, verbose_name='Критерий')
    description = models.CharField(max_length=500, verbose_name='Описание')
    value = models.CharField(max_length=500, verbose_name='Значение',
                             default='0')
    #
    # Номер пользователя*10 000 + номер теста * 100 + номер задания
    #
    number = models.PositiveIntegerField(verbose_name='Номер')

    @classmethod
    def create(cls, num_, crit, ans):
        answer = cls(
            criterion=crit,
            description=ans.description,
            value=ans.value,
            number=num_,
        )
        return answer

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Ответ'
        verbose_name_plural = 'Ответы'
        unique_together = ('number', 'criterion')
