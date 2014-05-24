from django.conf.urls import patterns, url, include
from flow_drawer import views
urlpatterns = patterns('',
	# ex: /flow_drawer/
	url(r'^$', views.index, name='index'),
	)
	