from django.urls import path, include, re_path
# from django.conf.urls import url
from rest_framework import routers

from . import views

# router = routers.SimpleRouter()
# router.register(r'page2', views.page2, basename='page2')

# urlpatterns = [
#     path('', views.index, name='index'),
#     re_path(r'^page2/', views.page2, name='page2')
# ]

urlpatterns = [
    # path('', include(router.urls)),
    path('', views.index, name='index'),
    # path('page2', views.page2, name='page2')
    re_path(r'^page2/', views.page2, name='page2')
]
