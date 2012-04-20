from django.conf.urls import patterns, include, url

urlpatterns = patterns('meep.views',
    # Examples:
    # url(r'^$', 'meepd.views.home', name='home'),
    # url(r'^meepd/', include('meepd.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^$', 'index'),
    url(r'^topics/$', 'topics'),
    url(r'^topics/add_topic/?$', 'add_topic'),
    url(r'^topics/(?P<topic_id>\d+)/?$', 'topic'),
    url(r'^topics/(?P<topic_id>\d+)/add_message/?$', 'add_message'),
    url(r'^topics/(?P<topic_id>\d+)/delete_message/?$', 'delete_message'),
    url(r'^topics/(?P<topic_id>\d+)/delete_topic/?$', 'delete_topic'),
)