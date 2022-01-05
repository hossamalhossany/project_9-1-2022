from django.db import connection
from django.shortcuts import render
from .models import test1
from .forms import contact_form
from .learn_python.lesson1 import hello


def index(request):
    html_file = 'polls/index.html'
    return render(request, html_file)


def page2(request):
    html_file = 'polls/page2.html'
    return render(request, html_file, {'contact_form': contact_form})


def page3(request):
    html_file = 'polls/page3.html'
    return render(request, html_file)


def put_data_to_databasa(request):
    test = test1()
    test.first_name = request.POST.get('first_name')
    test.last_name = request.POST.get('last_name')
    test.save()
    with connection.cursor() as cursor:
        sql = ''' select * from project_db.polls_test1 '''
        cursor.execute(sql)
        rows = cursor.fetchall()
    html_page = "polls/page2.html"
    return render(request, html_page, {'rows': rows})


def learn_python(request):
    data_learn = hello()
    data_learn2 = {'data_learn': data_learn}

    html_file = "polls/learn_python.html"
    return render(request, html_file, data_learn2)
