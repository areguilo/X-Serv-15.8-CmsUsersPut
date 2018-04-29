from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'cms.views.mainPage'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^login/', 'cms.views.loginView'),
	url(r'^logout/', 'cms.views.logoutView'),
    url(r'^authenticate/', 'cms.views.loginPage'),
    url(r'^(.*)', 'cms.views.contentPage'),

)
