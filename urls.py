from django.conf.urls.defaults import *

urlpatterns = patterns('mce_pygments.views',
    url(r'^$', 'pygments', name='pygments'),
)
