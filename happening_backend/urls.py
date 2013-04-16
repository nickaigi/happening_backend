from django.conf.urls import patterns, include, url
from core.api.resources import NewsResource, TagResource, UserResource
from tastypie.api import Api

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

v1_api = Api(api_name='v1')
v1_api.register(NewsResource())
v1_api.register(TagResource())
v1_api.register(UserResource())

urlpatterns = patterns('',

    url(r'^$', 'core.views.home', name='home'),
    #url(r'^core/', include('happening_backend.core.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'api/', include(v1_api.urls)),
)
