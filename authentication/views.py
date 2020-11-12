# Main Imports

# Django Imports
from django.shortcuts import render, get_object_or_404, HttpResponse
from django.http import HttpResponseRedirect
from django.core.exceptions import ObjectDoesNotExist
from django.core.files import File
from django.contrib.auth.models import User

# My Module Imports
from utils.auth_utils import get_banned_words


def signup_page(request):
    """
    users can use this page to signup to the platform and create accounts
    """
    # admin user session pop
    # admin user session pop
    # Deleting any sessions regarding top-tier type of users

    # Deleting sessions regarding basic users
    if "basic_user_email" in request.session:
        del request.session["basic_user_email"]
        del request.session["basic_user_username"]
        del request.session["basic_user_logged_in"]

    # Signup Form Processing
    invalid_credentials = False
    credentials_taken = False
    contains_space_in_credentials = False

    banned_words = get_banned_words()

    if request.POST.get("signup_submit_button"):
        email = request.POST.get("user_email")
        password = request.POST.get("password")
        re_entered_passwrod = request.POST.get("re_entered_passwrod")
        username = request.POST.get("username")

        # Check if username/email or password contains blank spaces " "
        for char in email:
            if char == " ":
                contains_space_in_credentials = True

        for char in username:
            if char == " ":
                contains_space_in_credentials = True

        for char in password:
            if char == " ":
                contains_space_in_credentials = True

        if contains_space_in_credentials == True:
            # do nothing since it has space
            pass
        else:
            # First check if any of the input are empty
            if bool(username) == False or username == "" \
               or bool(email) == False or email == "" \
               or bool(password) == False or password == "" \
               or bool(re_entered_passwrod) == False or re_entered_passwrod == "":
                invalid_credentials = True
            else:
                # check if the username or passowrd are the same
                if username == password:
                    invalid_credentials = True
                else:
                    # then check if the paswords match
                    if password != re_entered_passwrod:
                        invalid_credentials = True
                    else:
                        # then check if the username contains any banned words
                        contains_banned_words = False
                        for word in banned_words:
                            if word == username:
                                contains_banned_words = True
                        if contains_banned_words == True:
                            invalid_credentials = True
                        else:
                            print("continue")
                             # check if the same username or email exists if it
                            # does do not log it to the database it already exists


    # check if the password is in common passwords
    # ... havent implemented this yet

    # Preventing brute force
    # ... havent implemented this yet

    # check if the email is @...com
    # ... havent implemented this yet.

    data = {
        "invalid_credentials": invalid_credentials,
        "credentials_taken": credentials_taken,
        "contains_space_in_credentials": contains_space_in_credentials,
    }

    return render(request, "auth/signup.html", data)


def login_page(request):
    """

    """

    data = {

    }

    return render(request, "auth/login.html", data)
