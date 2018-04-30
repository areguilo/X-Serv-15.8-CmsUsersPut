from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cms.views.mainPage'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin', include(admin.site.urls)),
    url(r'^login', 'cms.views.my_view'),
	url(r'^logout', 'cms.views.logout_view'),
    url(r'^authenticate', 'cms.views.loginpage'),
    url(r'^(.*)', 'cms.views.contentPage'),
)
