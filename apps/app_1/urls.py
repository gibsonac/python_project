from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.index),
    url(r'^signup$', views.signup),
    url(r'^register$', views.register),
    url(r'^login_page$', views.login_page),
    url(r'^login$', views.login),
    url(r'^logout$', views.logout),
    url(r'^user/edit$', views.user_edit),
    url(r'^user/(?P<my_val>\d+)/edit$', views.user_submit_edit),
    url(r'^home$', views.home),
    url(r'^ocean_adventures$', views.ocean_adventures),
    url(r'^mountain_adventures$', views.mountain_adventures),
    url(r'^desert_adventures$', views.desert_adventures),
    url(r'^add_adventure$', views.add_adventure),
    url(r'^new_adventure$', views.new_adventure),
    url(r'^adventure/details/(?P<my_val>\d+)$', views.adventure_details),
]
