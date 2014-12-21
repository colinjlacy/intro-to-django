from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'cms.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # e.g.: /polls/
    url(r'^polls/', include('polls.urls', namespace='polls')),

    # e.g.: /admin/
    url(r'^admin/', include(admin.site.urls)),
)
