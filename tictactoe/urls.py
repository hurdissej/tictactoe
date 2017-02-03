from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.new_invitation, name='tictactoe_invite'),
    url(r'^invitation/(?P<pk>\d+)/$', views.accept_invitation, name='tictactoe_accept_invitation'),
    url(r'^game/(?P<pk>\d+)/$', views.game_detail, name='tictactoe_game_detail'),
    url(r'^game/(?P<pk>\d+)/do_move$', views.game_do_move, name='tictactoe_game_do_move')

]