from django.conf.urls import url
from . import views

app_name = 'dashboard'
urlpatterns = [
	url(r'^$', views.list_view, name="list"),
	url(r'^insert/$', views.insert_view, name="insert"),
	url(r'^update/(?P<update_id>[0-9]+)$', views.update_view, name="update"),
	url(r'^delete/(?P<delete_id>[0-9]+)$', views.delete_view, name="delete"),
]