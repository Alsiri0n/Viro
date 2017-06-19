from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.


class Region(models.Model):
    name = models.CharField(max_length=50, verbose_name='Район')

    def __str__(self):
        return self.name


class ViroUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    region = models.ForeignKey(Region, verbose_name='Район', default=1)
    REQUIRED_FIELDS = ['region']



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
#         def create_superuser(self, region, name, surname, patronymic, password):
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
