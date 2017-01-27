from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.new_invitation, name='tictactoe_invite'),
]