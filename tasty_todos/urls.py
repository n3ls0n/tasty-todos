from django.conf.urls import patterns, include, url
from tastypie.api import Api
from tasty_todos.views import index
from tasty_todos.resources import TodoResource
from settings import DEBUG

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(TodoResource())

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'tasty_todos.views.index', name='index'),
    (r'^api/', include(v1_api.urls)),
    # url(r'^tasty_todos/', include('tasty_todos.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)

if DEBUG:
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns
    urlpatterns += staticfiles_urlpatterns()
