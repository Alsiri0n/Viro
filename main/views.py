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
        if not self.request.user.is_staff:
            if self.request.user.pk is not None:
                context['criterions'] = CriterionList.objects.get(
                    id=ViroUser.objects.get(
                        user_id=self.request.user.id).criterionList.id).\
                    criterion.all()
        else:
            context['criterions'] = CriterionList.objects.get(pk=1).criterion.all()
        return context