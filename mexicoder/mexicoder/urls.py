from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers
from screen import views

router = routers.DefaultRouter()
router.register(r'leagues', views.LeagueViewSet)
router.register(r'teams', views.TeamViewSet)
router.register(r'couches',views.CoachViewSet)
router.register(r'players',views.PlayerViewSet)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'mexicoder.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
)
