from django.urls import path
from rest_framework import routers
from rest_framework.authtoken.views import obtain_auth_token
from .views import LogoutView


route = routers.DefaultRouter()


urlpatterns = [
    #path('', include(route.urls)),
    path('login/', obtain_auth_token, name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    
]
