from django.shortcuts import render
from django.views.generic import View, TemplateView


class HomeView(TemplateView):
    template_name = 'homepage.html'