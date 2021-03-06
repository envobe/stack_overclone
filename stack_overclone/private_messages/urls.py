from django.conf.urls import url
from . import views

app_name = 'private_messages'

urlpatterns = [
    url(r'^$',views.PrivateMessageList.as_view(),name='list'),
    url(r'^new/$',views.CreatePrivateMessage.as_view(),name='new_message'),
    url(r'^details/(?P<pk>\d+)/$',views.PrivateMessageDetail.as_view(),name='detail'),
    url(r'^delete/(?P<pk>\d+)/$',views.DeletePrivateMessage.as_view(),name='delete'),
]
