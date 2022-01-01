from django.shortcuts import render
from django.http import HttpResponseRedirect
from rest_framework import routers

# router = routers.DefaultRouter.register(r'page2', vipage2)


def index(request):
    html_file = 'polls/index.html'
    return render(request, html_file)


def page2():
    html_file = 'polls/page2.html'
    return HttpResponseRedirect(html_file)
    # return render(request, html_file)
