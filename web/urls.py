"""web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls import patterns, include, url
from django.conf.urls.static import static
from kdm.admin import *

from kdm.views import *
from notification.views import *
import settings
 
urlpatterns = patterns('',
    url(r'^$', home),
    url(r'^work/', include("kdm.links", namespace='projects')),
    url(r'^work/post/$',project_create),
    
    url(r'^contact/$',contact),
    url(r'^admin/', admin.site.urls),
    url(r'^blogs/', include("kdm.urls", namespace='posts')),
     url(r'^notification/', include("notification.urls")),
    url(r'^login/$', 'django.contrib.auth.views.login'),
    url(r'^logout/$', logout_page),
    url(r'^form/$', notify_form),
    url(r'^form/submitted$', form_submitted),
    #url(r'^accounts/login/$', 'django.contrib.auth.views.login'), # If user is not login it will redirect to login page
    #url(r'^register/$', register),
     #url(r'^register/success/$', register_success),
     url(r'^accounts/',include('registration.backends.simple.urls')),
    url(r'^home/$', home),
   url(r'^test/$', test),
   
) + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)