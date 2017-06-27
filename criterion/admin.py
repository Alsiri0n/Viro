from django.contrib import admin
from criterion.models import Criterion, CriterionList

# Register your models here.


class CriterionAdmin(admin.ModelAdmin):
    list_display = ('number', 'description','ages')
    fields = ('year', 'number', 'description',
              'ages', 'subject', 'goal', 'deadline', 'tools', 'responsible')

class CriterionListAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Criterion, CriterionAdmin)
admin.site.register(CriterionList, CriterionListAdmin)
