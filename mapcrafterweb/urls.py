from django.conf.urls import patterns, url
from django.views.generic.base import RedirectView
import views

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mapcrafterweb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r"^(|index.html)$", RedirectView.as_view(url="index")),
    url(r"^index$", views.index, name="index"),
    url(r"^downloads(?:/(?P<channel>main|nightly))?$", views.downloads, name="downloads"),
    url(r"^downloads\.json$", views.downloads_json, name="downloads.json")
)
