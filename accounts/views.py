from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import UserRegistrationForm
from .models import User
from .utils import set_random_username


def register_in_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username,
                            password=password)
        if user is not None:
            login(request, user)
            return redirect("home")

        context = {
            "error": "Ошибка! Проверьте username и password!"
        }
        return render(request=request, template_name="accounts/register_in.html", context=context)
    return render(request=request, template_name="accounts/register_in.html")


def register_up_view(request):
    form = UserRegistrationForm()

    if request.method == "POST":
        form = UserRegistrationForm(data=request.POST)
        try:
            if form.is_valid():
                username = form.cleaned_data['username']
                if not username:
                    username = set_random_username()
                user = User.objects.create(
                    username=username,
                    date_of_birth=form.cleaned_data['date_of_birth'],
                    email=form.cleaned_data['email'],
                )
                user.set_password(raw_password=form.cleaned_data['password'])
                user.save()
                login(request, user)
                return redirect("home")
        except KeyError:
            context = {
                'message': 'Make sure that you do not have mistakes!'
            }
            return render(request, "accounts/register_up.html", context)

    context = {
        "form": form
    }
    return render(request=request, template_name="accounts/register_up.html", context=context)


def logout_view(request):
    logout(request)
    return redirect('home')
