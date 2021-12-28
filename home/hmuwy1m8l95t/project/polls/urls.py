from django.urls import path,re_path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    re_path(r'^page2/', views.page2, name='page2')
]


