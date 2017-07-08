from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from criterion.models import CriterionList, Criterion
from answer.models import Answer
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name='Район')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'


class ViroUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, verbose_name='Район', default=None)
    criterionList = models.ForeignKey(CriterionList,
                                      verbose_name='Список критериев',
                                      default=None)
    number = models.PositiveSmallIntegerField(verbose_name="Ид")
    # criterion = models.ManyToManyField(
    #     Criterion,
    #     verbose_name='Критерии')
    # REQUIRED_FIELDS = ['region']


    def save(self, *args, **kwargs):
        if self.number<100:
            criterionlist = self.criterionList
            for crit in criterionlist.criterion.all():
                # user-year-crit 1 17 01=> 11 701
                curcritid = self.number * 10000 + (crit.year - 2000) * 100 +\
                            crit.number
                cur_crit = None
                if crit.number != curcritid:
                    cur_crit = Criterion.create(crit, curcritid)
                    cur_crit.save()
                    criterionlist.criterion.add(cur_crit)
                    criterionlist.criterion.remove(crit)
                    criterionlist.save()

                for ans in crit.answer_set.all():
                    # user-year-crit-ans: 1 17 01 01 1 170 101
                    curansid = self.number * 1000000 + (crit.year - 2000) * 10000 + \
                               crit.number * 100 + ans.number
                    if ans.number != curansid:
                        cur_ans = Answer.create(curansid, cur_crit, ans)
                        cur_ans.save()
        super(ViroUser, self).save(*args, **kwargs)

    class Meta:
        verbose_name = 'Работник'
        verbose_name_plural = 'Работники'
# @receiver(post_save, sender=User)
# def create_or_update_user_profile(sender, instance, created, **kwargs):
#     if created:
#         ViroUser.objects.create(user=instance)
#     instance.viroUser.save()


# Если решим делать свою модель аутентификации
# class ViroUserManager(BaseUserManager):
#     def create_user(self, region, name, surname, patronymic, password=None):
#         if not region:
#             raise ValueError('Выберите район')
#
#         user = self.model(
#             region = region,
#             name = name,
#             surname = surname,
#             patronymic = patronymic,
#         )
#
#         user.set_password(password)
#         user.save(using=self._db)
#         return user
#
#         def create_superuser(self, region, name, surname,
#  patronymic, password):
#             pass
#
#
# class ViroUser(AbstractBaseUser):
#     region = models.ForeignKey(Region, verbose_name="Район", max_length=50)
#     name = models.CharField(max_length=50)
#     surname = models.CharField(max_length=50)
#     patronymic = models.CharField(max_length=50)
#     is_active = models.BooleanField(default=True)
#     is_admin = models.BooleanField(default=False)
#     REQUIRED_FIELDS = ['name', 'surname', 'patronymic']
#
#
#
#     def has_perm(self, perm, obj=None):
#         return True
#
#     def has_module_perms(self, app_label):
#         return True
#
#     @property
#     def is_stuff(self):
#         return self.is_admin
