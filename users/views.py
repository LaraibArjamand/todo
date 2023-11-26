from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import redirect, render

from .forms import RegisterForm
from list.models import List



@login_required(login_url="/login")
def home_page(request):
    lists = List.objects.filter(user=request.user)
    return render(request, template_name="users/home.html", context={"lists": lists})


def sign_up(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        # if the user is logged in
        if request.user.is_authenticated:
            return redirect("home")
        form = RegisterForm()
    return render(request=request, template_name="users/register.html", context={"register_form":form})


def sign_in(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")
    else:      
        form = AuthenticationForm()
    return render(request=request, template_name="users/login.html", context={"login_form":form})


def signout(request):
    logout(request)
    messages.info(request, "You have successfully logged out.")
    return redirect("login") 