from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    if request.user.is_authenticated():
        return HttpResponseRedirect('/user/home')
    else:
        return render(request, "main/home.html")