from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied
from django.shortcuts import redirect

from .models import Invitation,  Game, Move
from .forms import InvitationForm, MoveForm

# Create your views here.
@login_required()
def new_invitation(request):
    if request.method == 'POST':
        invitation = Invitation(from_user=request.user)
        form = InvitationForm(data=request.POST, instance=invitation)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/home')
    else:
        form = InvitationForm()
    return render(request, "new_invitation.html", {'form': form})

@login_required()
def accept_invitation(request, pk):
    invitation = get_object_or_404(Invitation, pk=pk)
    if not request.user == invitation.to_user:
        raise PermissionDenied
    if request.method == 'POST':
        if "accept" in request.POST:
            game = Game.objects.new_game(invitation)
            game.save()
            invitation.delete()
            return HttpResponseRedirect(game)
        else:
            invitation.delete()
            return HttpResponseRedirect('/user/home')
    else:
        return render(request, "accept_invitation.html", {'invitation': invitation})


def game_detail(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if game.is_users_move(request.user):
        return redirect('tictactoe_game_do_move', pk=pk)
    return render(request, "game_detail.html", {'game': game})


def game_do_move(request, pk):
    game = get_object_or_404(Game, pk=pk)
    if not game.is_users_move(request.user):
        raise PermissionDenied
    context = {'game': game}
    if request.method == 'POST':
        form = MoveForm(data=request.POST, instance=game.create_move())
        context['form'] = form
        if form.is_valid():
            move = form.save()
            game.update_after_move(move)
            game.save()
            return redirect('tictactoe_game_detail', pk=pk)
    else:
        form=MoveForm()
        context['form'] = form
    return render(request, "game_do_move.html", context)