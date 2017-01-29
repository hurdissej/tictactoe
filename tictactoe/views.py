from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.exceptions import PermissionDenied

from .models import Invitation
from .forms import InvitationForm

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
            invitation.delete()
            return HttpResponseRedirect('/user/home')
        else:
            invitation.delete()
            return HttpResponseRedirect('/user/home')
    else:
        return render(request, "accept_invitation.html", {'invitation': invitation})