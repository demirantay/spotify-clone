from django.urls import path
from . import views

urlpatterns = [
    # Liked songs Page
    path("playlist/likes/", views.liked_songs, name="liked_songs"),
]
