from django.shortcuts import render
from django.http import HttpResponseRedirect


def index(request):
    html_file = 'polls/index.html'
    return render(request, html_file)


def page2():
    html_file = 'polls/page2.html'
    return HttpResponseRedirect(html_file)
    # return render(request, html_file)
