# -*- coding: utf-8 -*-
# FileName  : urls.py

from django.urls import path
from . import views

app_name = 'image_handle'
urlpatterns = [
    path('', views.index, name='index'),
    path('check/', views.check, name='check'),
    path('upload_img/', views.upload_img, name='upload_img'),
    path('check_img/', views.check_img, name='check_img'),
]

