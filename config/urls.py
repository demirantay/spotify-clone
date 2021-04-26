from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # Authentication App
    path("", include("authentication.urls")),

    # Home App
    path("", include("home.urls")),

    # Artists App
    path("", include("artist.urls")),

    # Playlist App
    path("", include("playlist.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
