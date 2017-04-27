#from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from . import views

#if settings.DEBUG:
#  import debug_toolbar

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.home, name = "home"),
    url(r'^logout/$', views.deconnexion),
    url(r'^login/$', views.connexion, name="connexion"),
    url(r'^activity/$', views.activity),
    url(r'^suppr_activity/(?P<ide>\d+)/$', views.suppr_activity),
    url(r'^leaderboard/$', views.leaderboard, name = "leaderboard"),
    url(r'^weekly/$', views.weekly),
    url(r'^liens_utiles/$', views.liens, name="liens"),
               #url(r'^__debug__/', include(debug_toolbar.urls)),
]

