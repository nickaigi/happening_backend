from django.conf.urls import patterns, include, url
from core.api.resources import NewsResource,TagResource, UserResource
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(NewsResource())
v1_api.register(TagResource())
v1_api.register(UserResource())

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'happening_backend.views.home', name='home'),
    # url(r'^happening_backend/', include('happening_backend.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/',include(v1_api.urls)),
)
