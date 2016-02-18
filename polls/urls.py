from django.conf.urls import patterns, url

from polls import views

urlpatterns = patterns('', 
	url(r'^$', views.index, name='index'),
	url(r'^view_2/$', views.view_2, name='view_2'),

)
