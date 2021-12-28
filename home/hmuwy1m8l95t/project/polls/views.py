from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    html_file = 'polls/index.html'
    # return HttpResponse("Hello, world. You're at the polls index. ya hossam 22 33 ")
    return render(request, html_file)


def page2(request):
    html_file = 'polls/page2.html'
    return render(request, html_file)