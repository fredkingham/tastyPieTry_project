from django.views.generic import TemplateView
from django.conf.urls.defaults import patterns
from main.api import BagResource, VegetableResource
from django.conf.urls.defaults import include
from django.conf.urls import url
from django.contrib import admin
admin.autodiscover()

bag_resource = BagResource()
vegetable_resource = VegetableResource()

urlpatterns = patterns('', 
    ('^$', TemplateView.as_view(template_name="index.html")),
    (r'^api/', include(bag_resource.urls)),
    (r'^api/', include(vegetable_resource.urls)),
    url(r'^admin', include(admin.site.urls)),
)
