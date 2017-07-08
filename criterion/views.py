from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from criterion.models import Criterion, CriterionList
from customuser.models import ViroUser, Region
from answer.models import Answer
from django import forms
from django.contrib import messages
from django.forms.models import modelformset_factory
from django.shortcuts import redirect,reverse
from django.core.exceptions import ValidationError
from itertools import chain
# Create your views here.


class AnswersForm(forms.ModelForm):
    template_name = "generic/form.html"
    error_css_class='error12'
    class Meta:
        model = Answer
        fields = ['description', 'value']

    description = forms.CharField(
        label='',
        widget=forms.Textarea(
            attrs={'readonly': 'readonly', 'class': 'output-area'})
    )
    value = forms.CharField(
        label='',
        widget=forms.TextInput(
            attrs={'class': 'input-area', 'required': True})
    )
    
    def clean(self):
        cleaned_data = super(AnswersForm, self).clean()
        if cleaned_data['description'] != 'Выводы':
            if not cleaned_data['value'].isdigit():
                for f in self.errors:
                    self.fields[f].widget.\
                        attrs.update(
                        {'class': self.fields[f].widget.attrs.get(
                        'class', '') + ' error'}
                        )
                raise ValidationError("Проверьте данные", code="invalid")
        return cleaned_data
    
    def is_valid(self):
        ret = forms.Form.is_valid(self)
        if (len(self.errors) == 1) and \
        (len(self.fields['value'].widget.attrs.get('class', '')) == 
        len('input-area')
        ):
            self.fields['value'].widget.attrs.update(
                {'class': self.fields['value'].widget.
                attrs.get('class', '') + ' error',
                 }
                )
        return ret
    
    def __init__(self, *args, **kwargs):
        super(AnswersForm, self).__init__(*args, **kwargs)
        if kwargs['instance'].description == 'Выводы':
            self.fields['value'].widget = \
                forms.Textarea(
                    attrs={'class': 'input-area',
                           'required': True,
                           'cols': 28,
                           'rows': 5,}
                )

AnswerFormSet = modelformset_factory(Answer, form=AnswersForm, extra=0)

# AnswerFormSet = formset_factory(Answer)


class CriterionView(TemplateView, CategoryListMixin):
    # success_message = "was created successfully"
    template_name = "criterionView.html"
    form = None

    def get_context_data(self, **kwargs):
        context = super(CriterionView, self).get_context_data(**kwargs)
        # Стафф
        context['staff'] = "asdasdasdasdasasas"
        # Для шапки
        context['criterion'] = Criterion.objects.get(pk=kwargs["criter_id"])
        # Для меню
        context['criterions'] = CriterionList.objects.get(
            pk=1).criterion.all()
        # Для шапки таблицы
        context['answersh'] = Answer.objects.filter(
            criterion_id=kwargs['criter_id']).values_list(
            'description', flat=True)
        context['region'] = Region.objects.all().\
            values_list('name', flat=True).order_by('name')
        qr = Region.objects.all().order_by('name')
        resultq = ()
        lend = 0
        for reg in qr:
            x = Answer.objects.filter(
            criterion_id=(
                Criterion.objects.filter(
                criterionlist=ViroUser.objects.filter(region=reg.id).values_list('criterionList')
                # criterionlist=1
                ))
            ).values_list('value', flat=True)

            # context['test_'+str(reg.id)+''] = list(chain((reg.name,), x))
            resultq = list(chain(resultq, (reg.name,), x))
            lend= len(x)+1
        context['data'] = resultq
        context['lend'] = lend
        return context



class CriterionUpdate(TemplateView, CategoryListMixin):
    template_name = "criterion.html"
    formset = None

    def get(self, request, *args, **kwargs):
        # answer = Answer.objects.get(criterion_id=self.kwargs['criter_id'])
        # self.formset = AnswersForm(instance=answer)
        # AnswerFormSet(
        #     # queryset=Answer.objects.get(id=1)
        # )
        formset = AnswerFormSet(
            queryset=Answer.objects.filter(
                criterion_id=kwargs['criter_id']),
                initial={}
        )
        self.formset = formset
        return super(CriterionUpdate, self).get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(CriterionUpdate, self).get_context_data(**kwargs)
        context['criterion'] = Criterion.objects.get(pk=kwargs["criter_id"])
        # context['criterions'] = Criterion.objects.all().order_by('number')
        context['criterions'] = CriterionList.objects.get(
            id=ViroUser.objects.get(
                user_id=self.request.user.id).criterionList.id).\
            criterion.all()
        context['formset'] = self.formset
        context['answers'] = Answer.objects.filter(
            criterion_id=kwargs['criter_id'])
        return context

    def post(self, request, *args, **kwargs):
        self.formset = AnswerFormSet(request.POST)
        if self.formset.is_valid():
            self.formset.save()
            messages.add_message(request, messages.SUCCESS, 'Сохранено')
            return redirect('criterion', kwargs['criter_id'])
        else:
            messages.add_message(request, messages.ERROR, 'Ошибка')
            return super(CriterionUpdate, self).get(request, *args, **kwargs)
