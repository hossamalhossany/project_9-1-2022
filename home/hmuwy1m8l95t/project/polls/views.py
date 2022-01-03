from django.shortcuts import render, HttpResponse
# from django.contrib.sites.shortcuts import get_current_site


def index(request):
    html_file = 'polls/index.html'
    return render(request, html_file)


def page2(request):
    # # html_file = 'polls/page2.html'
    # # html_file ='home/hmuwy1m8l95t/project.hossamweb.com/polls/templates/polls/page2.html'
    # html_file ='http://project.hossamweb.com/polls/page2.html'
    # return render(request, html_file)
    return HttpResponse("Hello, world. You're at the polls index. hhhhhhhhhh")
