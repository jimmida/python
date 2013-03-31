from django.conf.urls import patterns, url

from polls import views
from polls.models import Poll

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    )

