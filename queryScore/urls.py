from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^register/$', views.register, name='register'),
    url(r'^(?P<user_number>[0-9]+)/(?P<examtype>[a-zA-Z]+)/showpage/$', views.showpage, name='showpage'),
    url(r'^onQuery/$',views.onQuery, name='onQuery'),
    url(r'^onRegister$', views.onRegister, name='onRegister')

]