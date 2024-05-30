from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from .form import UserRegistrationForm
from .models import User
from .utils import set_random_username


def register_in_view(request):
    if request.method == "POST":  # получаем POST запрос с его данными
        username = request.POST.get("username")  # достаём из запроса username
        password = request.POST.get("password")  # достаём из запроса password
        user = authenticate(request, username=username,
                            password=password)  # проверяем username и password на существование
        if user is not None:  # Если пользователь с таким username и password найден
            login(request, user)  # авторизуем пользователя
            return redirect("home")  # перенаправляем его на главную страницу

        context = {
            "error": "Ошибка! Проверьте username и password!"
        }
        return render(request=request, template_name="accounts/register_in.html", context=context)
    return render(request=request, template_name="accounts/register_in.html")


def register_up_view(request):
    form = UserRegistrationForm()  # Определяется пустая форма для регистрации пользователя

    if request.method == "POST":  # Если пользователь ввёл данные в html форму и отправил их на сервер
        form = UserRegistrationForm(data=request.POST)  # передаём данные в форму
        if form.is_valid():  # форма проверяет данные
            username = form.cleaned_data['username']
            if not username:
                username = set_random_username()
            user = User.objects.create(  # создаём пользователя
                username=username,
                date_of_birth=form.cleaned_data['date_of_birth'],
                email=form.cleaned_data['email'],  # передаём пользователю email
            )
            user.set_password(raw_password=form.cleaned_data['password'])  # хешируем пароль пользователя
            user.save()  # сохранение пользователя
            login(request, user)
            return redirect("home")  # перенаправление пользователя на страницу авторизации

    context = {  # определение контекса
        "form": form
    }
    # отправка контекстных данных на html шаблон
    return render(request=request, template_name="accounts/register_up.html", context=context)


def logout_view(request):
    logout(request)
    return redirect('home')
