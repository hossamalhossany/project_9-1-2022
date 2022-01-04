from django.db import connection
from django.shortcuts import render
from .models import test1
from .forms import contact_form


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
        sql = ''' select * from mydb2.myapp_test1 '''
        cursor.execute(sql)
        rows = cursor.fetchall()
    html_page = "myapp/index.html"
    return render(request, html_page, {'rows': rows})

