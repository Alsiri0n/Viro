from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from criterion.models import Criterion, CriterionList
from customuser.models import ViroUser
from answer.models import Answer
from django import forms
from django.contrib import messages
from django.forms.models import modelformset_factory
from django.shortcuts import redirect,reverse
# Create your views here.


class AnswersForm(forms.ModelForm):
    class Meta:
        model = Answer
        fields = ['description', 'value']

    description = forms.CharField(
        label='Описание',
        widget=forms.Textarea(attrs={'readonly': 'readonly'})
    )
    value = forms.CharField(label='Значение')
    # criterion = Criterion.objects.filter(pk=1)

AnswerFormSet = modelformset_factory(Answer, form=AnswersForm, extra=0)

# AnswerFormSet = formset_factory(Answer)


class CriterionView(TemplateView, CategoryListMixin):
    template_name = "criterion.html"
    form = None

    def get_context_data(self, **kwargs):
        context = super(CriterionView, self).get_context_data(**kwargs)
        context['criterion'] = Criterion.objects.get(pk=kwargs["criter_id"])
        # context['criterions'] = Criterion.objects.all().order_by('number')
        context['criterions'] = CriterionList.objects.get(
            id=ViroUser.objects.get(
                region_id=self.request.user.id).criterionList.id).\
            criterion.all()
        context['answers'] = Answer.objects.filter(criterion_id =kwargs['criter_id'])
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
            queryset=Answer.objects.filter(criterion_id=kwargs['criter_id']),
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
                region_id=self.request.user.id).criterionList.id).\
            criterion.all()
        context['formset'] = self.formset
        context['answers'] = Answer.objects.filter(
            criterion_id=kwargs['criter_id'])
        return context

    def post(self, request, *args, **kwargs):
        self.formset = AnswerFormSet(request.POST)
        if self.formset.is_valid():
            self.formset.save()
            messages.add_message(request, messages.SUCCESS, 'Ответ добавлен')
            return redirect('criterion', kwargs['criter_id'])
        else:
            return super(CriterionUpdate, self).get(request, *args, **kwargs)
