import random

from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from account.forms import UserUpdateForm, ProfileUpdateForm  # UserProfileForm, UserPictureForm,
from account.models import Profile
from interviewer.models import Question

# Create your views here.
def login_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            return render(request, "login.html", {
                "error": "Invalid Username or Password."
            })


    return render(request, "login.html")


def register_request(request):
    if request.user.is_authenticated:
        return redirect("home")

    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]
        firstname = request.POST["firstname"]
        lastname = request.POST["lastname"]
        password = request.POST["password"]
        repassword = request.POST["repassword"]

        if repassword == password:
            if User.objects.filter(username=username).exists():
                return render(request, "register.html",  {
                    "error": "Username already exist.",
                    "username": username,
                    "email": email,
                    "firstname": firstname,
                    "lastname": lastname,
                })
            else:
                if User.objects.filter(email=email).exists():
                    return render(request, "register.html", {
                        "error": "E-Mail already exist.",
                        "username": username,
                        "email": email,
                        "firstname": firstname,
                        "lastname": lastname,
                    })
                else:
                    user = User.objects.create_user(username=username, email=email, first_name=firstname,
                                                    last_name=lastname, password=password)
                    user.save()
                    return redirect("login")

        else:
            return render(request, "register.html", {
                "error": "Password and Confirm Password do not match.",
                "username": username,
                "email": email,
                "firstname": firstname,
                "lastname": lastname,
            })


    return render(request, "register.html")


def logout_request(request):
    logout(request)
    return redirect("home")


def profile(request):
    profile_list = Profile.objects.all()

    if request.user.is_authenticated:
        return render(request, 'profile.html', {
            'profile_list': profile_list,

        })
    else:
        return redirect("login")


def profile_update(request):
    if request.method == "POST":
        u_form = UserUpdateForm(request.POST, instance=request.user)
        p_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.profile)

        if u_form.is_valid() and p_form.is_valid():
            u_form.save()
            p_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user)
        p_form = ProfileUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form,
        'p_form': p_form
    }

    return render(request, "update_user.html", context)


def retrieve_data(request):
    questions = Question.objects.all()
    return render(request, 'profile.html', {'questions': questions})
