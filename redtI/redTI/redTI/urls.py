from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('core.urls')),
    path('', include('users.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settinggs.MEDIA_URL, document_root=settings.MEDIA_ROOT)