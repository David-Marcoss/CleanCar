
from django.contrib import admin
from django.urls import include, path


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/acounts/', include('apps.acounts.urls')),
    path('api/v1/core/', include('apps.core.urls'))
    
]

