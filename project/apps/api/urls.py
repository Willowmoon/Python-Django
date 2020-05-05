from django.conf.urls import url, include
from rest_framework.urlpatterns import format_suffix_patterns
from apps.api.views import CreateJoke, DetailsView

urlpatterns = {
    url(r'^jokes/$', CreateJoke.as_view(), name="jokes"),
    url(r'^jokes/(?P<pk>\d+)/$',
        DetailsView.as_view(), name="joke-id"),
}

urlpatterns = format_suffix_patterns(urlpatterns)