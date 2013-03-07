from tastypie.resources import ModelResource
from tastypie import fields
from tastypie.resources import ALL, ALL_WITH_RELATIONS
from tastypie.authentication import Authentication
from tastypie.authorization import Authorization
from core.models import News, Tag
from django.contrib.auth.models import User


def remove_meta(data_dict):
    if isinstance(data_dict, dict):
        if 'meta' in data_dict:
            del(data_dict['meta'])

    return data_dict


class UserResource(ModelResource):
    """
    Resource for users
    """

    class Meta(object):
        queryset = User.objects.all()
        allowed_methods = ['get']
        resource_name = 'user'
        excludes = [
            'email', 'password', 'is_active', 'is_staff',
            'is_superuser', 'date_joined', 'last_login',
        ]
        authentication = Authentication()
        authorization = Authorization()
        include_resource_uri = False

    def alter_list_data_to_serialize(self, request, data_dict):
        return remove_meta(data_dict)


class NewsResource(ModelResource):
    """
    Resource for News Items
    """
    user = fields.ForeignKey(UserResource, 'user', full=True)

    class Meta:
        queryset = News.objects.all()
        allowed_methods = ['get', 'post']
        resource_name = 'news'
        filtering = {
            'user': ALL_WITH_RELATIONS,
        }
        excludes = ['slug', 'last_edited', ]
        authentication = Authentication()
        authorization = Authorization()
        include_resource_uri = False

    def alter_list_data_to_serialize(self, request, data_dict):
        return remove_meta(data_dict)


class TagResource(ModelResource):
    """
    Resource for Tags associated with News
    """
    news = fields.ForeignKey(NewsResource, 'news', full=True)

    class Meta:
        queryset = Tag.objects.all()
        allowed_methods = ['get']
        resource_name = 'tag'
        authentication = Authentication()
        authorization = Authorization()
        include_resource_uri = False
        excludes = ['last_edited', 'timestamp', ]
        filtering = {'title': ALL, 'news': ALL_WITH_RELATIONS, }

    def alter_list_data_to_serialize(self, request, data_dict):
        return remove_meta(data_dict)
