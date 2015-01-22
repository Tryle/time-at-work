from django.conf.urls import patterns, url
from django.views.generic import TemplateView

urlpatterns = patterns('',
    url(r'^$', TemplateView.as_view(template_name = 'schedule/home.html')),
    url(r'^overview$', TemplateView.as_view(template_name = 'schedule/home.html'), name = 'overview'),
    url(r'^statistics$', TemplateView.as_view(template_name = 'schedule/home.html'), name = 'statistics'),
)
