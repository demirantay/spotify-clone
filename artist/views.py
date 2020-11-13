# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from authentication.models import BasicUserProfile

from utils.session_utils import get_current_user, get_current_user_profile


def artist_page(request, name):
    """
    in this page the users can see the specific pages of different artists
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop


    data = {

    }

    return render(request, "artist/artist_page.html", data)
