from django.conf.urls import patterns, url, include
from rest_framework.routers import DefaultRouter

from tweeter import views


router = DefaultRouter()
router.register(r'tweets', views.TweetViewSet)
router.register(r'users', views.UserViewSet)

urlpatterns = patterns('',
                       url(r'^api/', include(router.urls),
                           url(r'^$', views.index, name='index'),
                           url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
                       ))
