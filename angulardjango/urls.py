from django.conf.urls import patterns, include, url
from rest_framework.routers import DefaultRouter
from django.contrib import admin

from tweeter import views


admin.autodiscover()

router = DefaultRouter()
router.register(r'tweets', views.TweetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       url(r'^admin/', include(admin.site.urls)),
                       url(r'^api/', include(router.urls)),
                       url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       url(r'^$', views.index, name='index'),
)


