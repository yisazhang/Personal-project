"""PersonalInformation URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from PersonalInformation.view import person
from PersonalInformation.view import personal_list
from PersonalInformation.view import personal_delete
from PersonalInformation.view import personal_update_html
from PersonalInformation.view import personal_update

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url('^person/$',person),
    url('^personal_list/$',personal_list),
    url('^personal_delete/$',personal_delete),
    url('^personal_update_html/$',personal_update_html),
    url('^personal_update/$',personal_update),
]
