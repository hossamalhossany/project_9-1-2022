from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('page2/', views.page2, name='page2'),
    path('page3/', views.page3, name='page3'),
    path('put_data_to_databasa', views.put_data_to_databasa, name='put_data_to_databasa'),

]
