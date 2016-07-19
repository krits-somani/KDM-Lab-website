from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static

from .views import (
		post_create,
		post_update,
		post_delete,
		index,
		project_create,
		view_post

	)


urlpatterns = patterns('',
	url(r'^create/$', post_create),
	url(r'^$', "kdm.views.index", name="list"),
	 url(r'^view/(?P<id>\d+)/$', 'kdm.views.view_post', name='view_blog_post'),
	url(r'^view/(?P<id>\d+)/edit/$', post_update, name='update'),
	url(r'^view/(?P<id>\d+)/delete/$', post_delete, name="delete"),
)