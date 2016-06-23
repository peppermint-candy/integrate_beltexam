from django.conf.urls import url, include
from . import views

urlpatterns = [
	url(r'^$', vies.realindex, name = "indexreally")
    url(r'^products$', views.index , name = "main"),
    url(r'^products/show/(?P<id>[0-9]+$)', views.show, name = "show"),
    url(r'^products/(?P<id>[0-9]+)edit$', views.edit, name = "edit"),
    url(r'^products/new$', views.new , name = "new"),
    url(r'^products/destroy$', views.destroy, name = "destroy"),
    url(r'^products/create$', views.create , name = "create"),

]
