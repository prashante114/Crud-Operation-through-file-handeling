from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('access_session', views.access_session, name='access_session'),
    path('fees_view', views.file_crud_operation, name='access_session'),
    url(r'^record_delete/(?P<username>\w+)/$',views.record_delete,name='record_delete'),
]