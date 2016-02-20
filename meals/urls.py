from django.conf.urls import url
from . import views

urlpatterns = [
  # Nick's test page
  url(r'^demo/', views.demo, name='demo'),

  # App homepage
  url(r'^$', views.index, name='index'),
]