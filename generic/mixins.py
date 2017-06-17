from django.views.generic.base import ContextMixin


class CategoryListMixin(ContextMixin):
    def get_context_data(self, **kwargs):
        context = super(CategoryListMixin, self).get_context_data(**kwargs)
        context["current_url"] = self.request.path
        return context


class PagNumberMixin(CategoryListMixin):
    def get_context_data(self, **kwargs):
        context = super(PagNumberMixin, self).get_context_data(**kwargs)
        try:
            context["pn"] = self.request.GET["page"]
        except:
            context["pn"] = "1"
        return context