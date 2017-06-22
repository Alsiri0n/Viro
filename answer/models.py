from django.db import models
from criterion.models import Criterion
# Create your models here.


class Answer(models.Model):
    criterion = models.ForeignKey(Criterion)
    description = models.CharField(max_length=500, verbose_name='Название')
    value = models.CharField(max_length=500, verbose_name='Значение')

    def __str__(self):
        return self.description

    class Meta:
        verbose_name = 'Вопрос'
        verbose_name_plural = 'Вопросы'
