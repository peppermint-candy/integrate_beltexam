from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name = "usermain"),
    url(r'^login$', views.login, name= "userlogin"),
    url(r'^register$', views.register, name = "userregist"),
    url(r'^enter$', views.processLogin, name = "prologin"),
    url(r'^regist$', views.processRegist, name = "proregist"),
    url(r'^dashboard$', views.dashboard, name = 'dashboard' ),
    url(r'^signout$', views.signout, name = "signout"),
    url(r'^users/edit/(?P<id>\d+)$', views.edit, name = "edit"),
    url(r'^users/edit/(?P<id>\d+)/process$', views.proedit, name="proedit"),
    url(r'^users/show/(?P<id>\d+)$', views.show ),
]
