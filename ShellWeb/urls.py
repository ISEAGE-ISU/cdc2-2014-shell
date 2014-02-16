from django.conf.urls import patterns, include, url
from Blog.views import frontpage, single_post
from Home.views import home, clients, about, debug
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ShellWeb.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r"^/(?P<post_id>\d+)/$", single_post, name="post"),
    url(r'^$', home, name="Home" ),
    url(r'^clients/', clients, name="Clients"),
    url(r'^about/', about, name="About"),
    url(r'^blog/', frontpage, name="blog"),
    url(r'^blog/view/(?P<post_id>[^\.]+)', single_post, name='single_post'),
    url(r'^debug/', debug, name='debugging'),
)
