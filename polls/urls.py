from django.conf.urls import url
from . import views

app_name = 'polls'
urlpatterns = [
    url('^$',views.index),
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
    url(r'^export/$', views.export, name='export'),
    url(r'^upload/$', views.upload, name='upload'),
    url(r'^sendmail/$', views.send_mail, name='sendmail'),
    url(r'^author_add/$',views.author_add,name='author_add'),
    url(r'^publisher_add/$',views.publisher_add,name='publisher_add'),

]
