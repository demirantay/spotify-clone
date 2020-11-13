from django.urls import path
from . import views

urlpatterns = [
    # Artists Page
    path("artist/<str:name>/", views.artist_page, name="artist_page"),
]
