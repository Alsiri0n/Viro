from django.conf.urls import url
from criterion.views import CriterionView, CriterionUpdate


urlpatterns = [
    url(r'^(?P<criter_id>\d+)/?$', CriterionUpdate.as_view(), name="criterion")
]