"""Appraise URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from django.conf.urls import url, handler404, handler500
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.contrib.auth.decorators import login_required
from Dashboard import views as dashboard_views
from Appraise.settings import BASE_CONTEXT

# Base context for all views.
#BASE_CON3TEXT = {
#  'commit_tag': '#wmt17dev',
#  'title': 'Appraise evaluation system',
#  'static_url': STATIC_URL,
#}

# HTTP error handlers supporting COMMIT_TAG.
handler404 = 'Dashboard.views._page_not_found'
handler500 = 'Dashboard.views._server_error'

# pylint: disable=C0330
urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^$', dashboard_views.frontpage, name='frontpage'),
    url(r'^dashboard/create-profile/$',
      dashboard_views.create_profile,
      name='create-profile'
    ),

    url(r'^dashboard/sign-in/$',
      auth_views.LoginView.as_view(
        template_name='Dashboard/signin.html',
        extra_context=BASE_CONTEXT
      ),
      name='sign-in'
    ),

    url(r'^dashboard/sign-out/$',
      auth_views.LogoutView.as_view(
        template_name='Dashboard/signout.html', # TODO: this does not exist!
        extra_context=BASE_CONTEXT
      ),
      name='sign-out'
    ),

    url(r'^dashboard/change-password/$',
      auth_views.PasswordChangeView.as_view(
        template_name='Dashboard/change-password.html',
        success_url='/dashboard/',
        extra_context=BASE_CONTEXT
      ),
      name='change-password'
    ),

    url(r'^dashboard/update-profile/$',
      dashboard_views.update_profile,
      name='update-profile'
    ),

    url(r'^dashboard/$', dashboard_views.dashboard, name='dashboard'),
]
