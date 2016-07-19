from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from .views import (
		work,
		project_create,

	)


urlpatterns = patterns('',
	url(r'^post/$', project_create),
	url(r'^$', "kdm.views.work", name="pro"),
	# url(r'^view/(?P<id>\d+)/edit/$', post_update, name="update"),
	# url(r'^view/(?P<id>\d+)/delete/$', post_delete, name="delete"),
)