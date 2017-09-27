from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.person_list, name='person_list'),
    url(r'^new$', views.person_create, name='person_new'),
    url(r'^edit/(?P<pk>\d+)$', views.person_update, name='person_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.person_delete, name='person_delete'),
]

