from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.UniversityListView.as_view(), name='list'),
    url(r'^(?P<pk>[\w]+)/update/$', views.UniversityUpdateView.as_view(), name='update'),

]