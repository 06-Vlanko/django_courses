from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^add_course/$', views.addCourse),
    url(r'^destroy/(?P<course_id>\d+)/$', views.destroy),
    url(r'^yes_destroy/(?P<course_id>\d+)/$', views.yes_destroy)
]