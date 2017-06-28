from django.shortcuts import render
from django.views.generic.base import TemplateView
from generic.mixins import CategoryListMixin
from criterion.models import Criterion, CriterionList
from customuser.models import ViroUser
# Create your views here.


class MainPageView(TemplateView, CategoryListMixin):
    template_name = "mainpage.html"
    def get_context_data(self, **kwargs):
        context = super(MainPageView, self).get_context_data(**kwargs)
        # context['criterions'] = Criterion.objects.all().order_by('number')
        print ("test")
        if self.request.user.pk is not None:
            context['criterions'] = CriterionList.objects.get(
                id=ViroUser.objects.get(
                    region_id=self.request.user.id).criterionList.id).criterion.all()
        return context