from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home),
    url(r'^logout/$', views.deconnexion),
    url(r'^login/$', views.connexion, name="connexion"),
    url(r'^activity/$', views.activity),
    url(r'^suppr_activity/(?P<id>\d+)/$', views.suppr_activity),
    url(r'^leaderboard/$', views.leaderboard),
    url(r'^previousweeks/$', views.previousweeks),
    url(r'^liens_utiles/$', views.liens),
]
