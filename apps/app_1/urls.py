from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup),
    url(r'^register$', views.register),
    url(r'^login$', views.login),
    url(r'^ocean_adventures$', views.ocean_adventures),
    url(r'^mountain_adventures$', views.mountain_adventures),
    url(r'^desert_adventures$', views.desert_adventures),
]
