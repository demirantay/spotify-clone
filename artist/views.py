# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from authentication.models import BasicUserProfile


def artist_page(request, artist_name):
    """
    users can use this page to signup to the platform and create accounts
    """

    data = {}

    return render(request, "artist/artist.html", data)
