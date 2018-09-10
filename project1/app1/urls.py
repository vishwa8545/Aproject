from django.conf.urls import url,include
from django.contrib.auth.views import login,logout
from . import views

urlpatterns = [

    url(r'^index/',views.index),
    url(r'^home/',views.home),
    url(r'^users/',views.user),
    url(r'^login/',login,{'template_name':'login.html'}),
    url(r'^logout/',logout,{'template_name':'logout.html'}),
    url(r'^signup/',views.register),
]
