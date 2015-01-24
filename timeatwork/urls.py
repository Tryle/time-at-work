from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'timeatwork.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^', include('schedule.urls')),
)

urlpatterns += staticfiles_urlpatterns()
