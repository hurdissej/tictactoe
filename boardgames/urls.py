"""boardgames URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from django.contrib.auth import views as auth_views
admin.autodiscover()

urlpatterns = [
    url(r'^$', include('main.urls'), name='boardgames_home'),
    url(r'^admin/', admin.site.urls),
    url(r'^tictactoe/', include('tictactoe.urls')),
    url(r'^login',auth_views.login,{'template_name': 'registration/login.html'}, name='boardgames_login'),
    url(r'^logout/',auth_views.logout,{'next_page': 'index'}, name='boardgames_logout'),
    url(r'^user/', include('user.urls')),
    ]
