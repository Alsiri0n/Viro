from django.conf.urls import url
from criterion.views import CriterionView, CriterionUpdate


urlpatterns = [
    url(r'^(?P<criter_id>\d+)/?$', CriterionUpdate.as_view(), name="criterion"),
    url(r'^(?P<criter_id>\d+)/staff?$', CriterionView.as_view(), name="criterionView"),
]