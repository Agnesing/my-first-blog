# -*- coding: utf-8 -*-
"""
Created on Sun May 24 10:21:11 2020

@author: E7240
"""

from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
]