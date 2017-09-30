from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.person_list, name='person_list'),
    url(r'^new$', views.person_create, name='person_new'),
    url(r'^edit/(?P<pk>\d+)$', views.person_update, name='person_edit'),
    url(r'^delete/(?P<pk>\d+)$', views.person_delete, name='person_delete'),

    url(r'^banks$', views.bank_list, name='bank_list'),
    url(r'^newbank$', views.bank_create, name='bank_new'),
    url(r'^editbank/(?P<pk>\d+)$', views.bank_update, name='bank_edit'),
    url(r'^deletebank/(?P<pk>\d+)$', views.bank_delete, name='bank_delete'),
]

