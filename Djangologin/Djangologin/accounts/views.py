
import re
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


def login_view(request):
    error = ""

    if request.method == "POST":
        username = request.POST.get("username", "").strip()
        password = request.POST.get("password", "")

        # Validate username using regular expression
        if not re.fullmatch(r"[A-Za-z0-9_]{3,20}", username):
            error = "Username must contain 3-20 letters, digits or underscores."

        # Validate password format
        elif not re.fullmatch(r"(?=.*[A-Za-z])(?=.*\d)\S{8,}", password):
            error = "Password needs at least 8 characters, a letter and a digit."

        else:
            # Verify credentials using Django authentication
            user = authenticate(
                request,
                username=username,
                password=password
            )

            if user is not None:
                login(request, user)
                return redirect("home")
            else:
                error = "Invalid username or password."

    return render(request, "login.html", {"error": error})


@login_required
def home(request):
    return render(request, "home.html")


def logout_view(request):
    logout(request)
    return redirect("login")
