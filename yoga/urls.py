from django.conf.urls import include, url
from django.contrib import admin
from . import views

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name = "home"),
    url(r'^logout/$', views.deconnexion, name="logout"),
    url(r'^login/$', views.connexion, name="connexion"),
    url(r'^activity/$', views.activity, name = "activity"),
    url(r'^suppr_activity/(?P<id>\d+)/$', views.suppr_activity),
    url(r'^leaderboard/$', views.leaderboard, name = "leaderboard"),
    url(r'^previousweeks/$', views.previousweeks, name = "personalhistory"),
    url(r'^liens_utiles/$', views.liens, name="liens"),
]
