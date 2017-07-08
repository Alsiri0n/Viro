from django.contrib import admin
from answer.models import Answer

# Register your models here.


class AnswerAdmin(admin.ModelAdmin):
    list_display = ('number', 'criterion', 'description')
    ordering = ('criterion', 'number',)

admin.site.register(Answer, AnswerAdmin)
