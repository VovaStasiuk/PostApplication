from django.contrib import admin
from django.urls import path, include


apipatterns = [
    path('', include('apps.posts.api.urls')),
    path('account/', include('apps.accounts.api.urls')),
]

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(apipatterns)),
]
