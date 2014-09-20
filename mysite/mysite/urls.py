from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^flow_drawer/',include('flow_drawer.urls',namespace="flow_drawer")),
    url(r'^blog/',include('blogapp.urls',namespace="blogapp")),
)
