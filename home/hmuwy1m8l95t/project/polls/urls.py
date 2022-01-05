from django.urls import path
from .views import index, page2, page3, put_data_to_databasa, learn_python

urlpatterns = [
    path('', index, name='index'),
    path('page2/', page2, name='page2'),
    path('page3/', page3, name='page3'),
    path('page2/put_data_to_databasa/', put_data_to_databasa, name='put_data_to_databasa'),
    path('learn_python/', learn_python, name='learn_python'),

]
