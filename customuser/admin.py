from django.contrib import admin
from customuser.models import Region, ViroUser
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

# Register your models here.

admin.site.register(Region)


class ViroInline(admin.StackedInline):
    model = ViroUser
    can_delete = False
    verbose_name = 'Район'
    # verbose_name_plural = 'Сотрудники'
    # list_display = ('Region.name')


class UserAdmin(BaseUserAdmin):
    inlines = (ViroInline, )



admin.site.unregister(User)
admin.site.register(User, UserAdmin)
