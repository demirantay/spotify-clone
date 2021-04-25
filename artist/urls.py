from django.urls import path
from . import views

urlpatterns = [
    # signup Page
    path("artist/<str:artist_name>/", views.artist_page, name="artist_page"),
]
