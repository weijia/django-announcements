from django.conf.urls.defaults import *


urlpatterns = patterns("",
    url(r"^(?P<pk>\d+)/$", "announcements.views.detail", name="announcements_detail"),
    url(r"^(?P<pk>\d+)/hide/$", "announcements.views.dismiss", name="announcement_dismiss")
)
