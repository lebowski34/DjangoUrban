from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
from django.http import HttpResponse
from .forms import UserRegister

def sign_up_by_django(request):
    users = ("Alex", "Jo")
    if request.method == "POST":
        form = UserRegister(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            repeat_password = form.cleaned_data['repeat_password']
            age = form.cleaned_data['age']
            if username in users:
                error = "Пользователь уже существует"
                info = {
                    'error': error
                }
                return render(request, "fifth_task/registration_page.html", info)
            if password != repeat_password:
                error = "Пароли не совпадают"
                info = {
                    'error': error
                }
                return render(request, "fifth_task/registration_page.html", info)
            if int(age) <= 17:
                error = "Возраст должен быть 18+"
                info = {
                    'error': error
                }
                return render(request, "fifth_task/registration_page.html", info)
            return HttpResponse(f"Добро пожаловать, {username}")
    else:
        form = UserRegister()
    return render(request, "fifth_task/registration_page.html", {'form': form})