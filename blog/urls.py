from django.conf.urls import patterns, url, include
import views as blog_views
from django.conf import settings

urlpatterns = patterns('',
                       url(r'^$', blog_views.index),
                       url(r'^about/', blog_views.about_page),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/$', blog_views.category, name='category'),
                       url(r'^add_category/', blog_views.add_category, name='add_category'),
                       url(r'^category/(?P<category_name_slug>[\w\-]+)/add_page/', blog_views.add_page, name='add_page'),
                       url(r'^register/$', blog_views.register, name='register')
                       )


if settings.DEBUG:
    print 'debug is true'
    urlpatterns += patterns(
        'django.views.static',
        (r'media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
    print urlpatterns
