from django.shortcuts import render
from django.template.response import TemplateResponse
from django.views.generic import TemplateView
# Create your views here.

class menu(TemplateView):
    template_name = 'fourth_task/menu.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_title'] = 'Главная страница'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'
        return context

class cart_temp(TemplateView):
    template_name = 'fourth_task/cart.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_title'] = 'Корзина'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'
        return context

class games_temp(TemplateView):
    template_name = 'fourth_task/games.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_title'] = 'Игры'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'
        return context

class platform_temp(TemplateView):
    template_name = 'fourth_task/platform.html'
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['main_title'] = 'Главная страница'
        context['main'] = 'Главная'
        context['shop'] = 'Магазин'
        context['cart'] = 'Корзина'
        return context