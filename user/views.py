from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.

from tictactoe.models import Game

@login_required()
def home(request):
    my_games = Game.objects.games_for_user(request.user)
    active_games = my_games.filter(status="A")
    finished_games = my_games.exclude(status="A")
    waiting_games = my_games.filter(next_to_move = request.user)
    other_games = my_games.exclude(next_to_move = request.user)
    context = {
        "other_games": other_games,
        "waiting_games": waiting_games,
        "finished_games": finished_games,

    }
    return render(request, "user/home.html", context)