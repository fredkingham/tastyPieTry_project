import datetime
from dateutil.parser import parse
from decimal import Decimal
import re
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from django.utils import datetime_safe, importlib
from django.core.urlresolvers import resolve
from tastypie.bundle import Bundle
from tastypie.exceptions import ApiFieldError, NotFound
from tastypie.utils import dict_strip_unicode_keys, make_aware
from tastypie.resources import ModelResource
from main.models import Bag, Vegetable
from tastypie import fields
from tastypie.authorization import Authorization


class AllowAllAuthorization(Authorization):
    def delete_list (self, object_list, bundle):
        return object_list
        
    def delete_detail (self, object_list, bundle):
        return True
        

class BagResource(ModelResource):
    # attending_status = fields.ToManyField('mainPage.api.AttendingStatusResource', 'attending_statuses', related_name = 'event')
    vegetables = fields.ToManyField("main.api.VegetableResource", 'vegetables', null=True, blank=True)
    class Meta:
        queryset = Bag.objects.all()
        resource_name = 'bags'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = AllowAllAuthorization()


class VegetableResource(ModelResource):
    bag = fields.ToOneField(BagResource, 'bag')

    class Meta:
        queryset = Vegetable.objects.all()
        resource_name = 'vegetables'
        list_allowed_methods = ['get', 'post', 'put', 'delete']
        detail_allowed_methods = ['get', 'post', 'put', 'delete']
        authorization = AllowAllAuthorization()
