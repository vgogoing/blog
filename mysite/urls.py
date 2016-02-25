from django.conf.urls import patterns, include, url
from django.contrib import admin
from blog import urls as blog_url
from django.conf import settings


urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mysite.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^blog/', include(blog_url))

)
#
# if settings.DEBUG:
#     print 'debug is true'
#     urlpatterns += patterns(
#         'django.views.static',
#         (r'^media/(?P<path>.*)',
#         'serve',
#         {'document_root': settings.MEDIA_ROOT}), )
#     print urlpatterns
