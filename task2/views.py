from django.views.generic import TemplateView
from django.shortcuts import render
from django.views import View

class class_temp(TemplateView):
    template_name = 'second_task/class_template.html'

class func_temp(TemplateView):
    template_name = 'second_task/func_template.html'