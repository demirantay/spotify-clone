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


def index(request):
    """
    this is the landing page of the app and handles most of the redirecton
    when the access control is right. But if no user is registered or logged
    in the sessions it just returns the basic static landing page.
    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop

    # Get the current users
    current_basic_user = get_current_user(request, User, ObjectDoesNotExist)

    current_basic_user_profile = get_current_user_profile(
        request,
        User,
        BasicUserProfile,
        ObjectDoesNotExist
    )

    if current_basic_user != None and current_basic_user_profile != None:
        return HttpResponseRedirect("/home/")

    data = {

    }

    return render(request, "home/index.html", data)


def home(request):
    """

    """
    # Deleting any sessions regarding top-tier type of users
    # session.pop("programmer_username", None)  <-- these are flask change it
    # session.pop("programmer_logged_in", None) <-- these are flask change it
    # admin user session pop
    # admin user session pop


    data = {

    }

    return render(request, "home/home.html", data)
