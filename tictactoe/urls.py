from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.new_invitation, name='tictactoe_invite'),
    url(r'^invitation/(?P<pk>\d+)/$', views.accept_invitation , name='tictactoe_accept_invitation')
]