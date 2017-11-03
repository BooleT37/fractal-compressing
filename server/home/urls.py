from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^upload_target_image', views.upload_target_image, name='upload_target_image'),
    url(r'^upload_blank_image', views.upload_blank_image, name='upload_blank_image'),
    url(r'^recode_image', views.recode_image, name='recode_image'),
    url(r'^iterate_recode', views.iterate_recode, name='iterate_recode'),
    url(r'^$', views.index, name='index')
]