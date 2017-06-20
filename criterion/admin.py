from django.contrib import admin
from criterion.models import Criterion

# Register your models here.


class CriterionAdmin(admin.ModelAdmin):
    list_display = ('number', 'description','ages')


admin.site.register(Criterion, CriterionAdmin)
