from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import SetPasswordForm
from django.contrib import messages
from .forms import UserRegistrationForm, LoginForm
from .models import User

def register_view(request):
    form = UserRegistrationForm(request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        user = form.save()
        login(request, user)
        return redirect("users:home")
    return render(request, "users/create_account.html", {"form": form})

def login_view(request):
    form = LoginForm(request, data=request.POST if request.method == "POST" else None)
    if request.method == "POST" and form.is_valid():
        user = authenticate(
            request, 
            username=form.cleaned_data["username"], 
            password=form.cleaned_data["password"]
        )
        if user:
            login(request, user)
            return redirect("users:home")
        messages.error(request, "Usuario o contraseña incorrectos")
    return render(request, "users/login.html", {"form": form})

@login_required
def home_view(request):
    return render(request, "home.html")

def password_reset_view(request):
    user_id = request.session.get("reset_user_id")
    form = None

    if request.method == "POST":
        if "username" in request.POST:
            user = User.objects.filter(username=request.POST.get("username")).first()
            if user:
                request.session["reset_user_id"] = user.id
                return redirect("users:password_reset")
            messages.error(request, "El usuario no existe")

        elif "new_password1" in request.POST and user_id:
            user = get_object_or_404(User, id=user_id)
            form = SetPasswordForm(user, request.POST)
            if form.is_valid():
                form.save()
                request.session.pop("reset_user_id", None)
                messages.success(request, "Contraseña restablecida con éxito. Ahora puedes iniciar sesión.")
                return redirect("login")
            messages.error(request, "Hubo un error con la contraseña")

    if user_id:
        user = get_object_or_404(User, id=user_id)
        form = SetPasswordForm(user)

    return render(request, "users/password_reset.html", {"form": form})
