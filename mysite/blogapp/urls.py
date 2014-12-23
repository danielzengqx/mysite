from django.conf.urls import patterns, url, include
from blogapp import views
urlpatterns = patterns('',
	url(r'^$', views.index, name='index'),
        url(r'^update/',  views.update, name='update'),
        url(r'^delete/',  views.delete, name='delete'),
        url(r'^update/',  views.update, name='update'),
        url(r'^mysubmit/',  views.mysubmit, name='mysubmit'),
        
	)
