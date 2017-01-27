from django.shortcuts import render
from django.contrib.auth.decorators import  login_required
from django.http import HttpResponseRedirect
from .models import Invitation
from .forms import InvitationForm

# Create your views here.
@login_required()
def new_invitation(request):
    if request.method == 'POST':
        form = InvitationForm(data=request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/user/home')
    else:
        form = InvitationForm()
    return render(request, "new_invitation.html", {'form': form})