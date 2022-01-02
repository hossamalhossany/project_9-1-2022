from django.shortcuts import render
from rest_framework import routers


def index(request):
    html_file = 'polls/index.html'
    return render(request, html_file)


def page2(request):
    html_file = 'polls/page2.html'
    return render(request, html_file)
