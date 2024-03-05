from django.urls import include, path
from .api.vewsets import UserViewSet,UserCreateViewSet

from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token


route = routers.DefaultRouter()

#route.register(r'user',UserViewSet, basename='users')


urlpatterns = [
    path('', include(route.urls)),
    path('create', UserCreateViewSet.as_view(), name='user-create'),
    path('<int:pk>', UserViewSet.as_view(), name='user'),
    
]
urlpatterns += route.urls