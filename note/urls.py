from django.conf.urls import url

from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^/?P<id>[a-zA-Z0-9]{8}', views.get_note, name='get_note'),
]