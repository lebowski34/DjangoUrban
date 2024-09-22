from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View

# Классовое представление для class_template.html
class class_temp(TemplateView):
    template_name = 'second_task/class_template.html'

# Функциональное представление для func_template.html
def func_temp(request):
    return render(request, 'second_task/func_template.html')
