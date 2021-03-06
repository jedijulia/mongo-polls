from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('',
    url(r'^$', views.IndexView.as_view(), name='index'),
    url(r'^(?P<pk>[0-9a-z]*)/$', views.DetailView.as_view(), name='detail'),
    url(r'^(?P<pk>[0-9a-z]*)/results/$', views.ResultsView.as_view(), name='results'),
    url(r'^(?P<poll_id>[0-9a-z]*)/vote/$', views.vote, name='vote'),
)

#urlpatterns = patterns('',
    # ex: /polls/
    #url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    #url(r'^(?P<poll_id>[0-9a-z]*)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    #url(r'^(?P<poll_id>[0-9a-z]*)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    #url(r'^(?P<poll_id>[0-9a-z]*)/vote/$', views.vote, name='vote'),
#)

