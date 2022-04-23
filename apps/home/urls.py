# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.urls import path, re_path
from apps.home import views
from django.views.generic import TemplateView

urlpatterns = [

    # The home page
    path('', views.landing, name='home'),
    path('index', views.index, name='index'),
    path('product', views.product, name='product'),
    path('creator', views.creator, name='creator'),
    path('profile', views.profile, name='profile'),
    path('requested/categories/', views.categoryrequest, name='categoryrequest'),
    path('all/feedbacks', views.viewfeedback, name='viewfeedback'),
    path('category/new/', views.newcategory, name='newcategory'),
    path('your/valuable/feedback', views.feedback, name='feedback'),
    path('upload/new/nft/', views.newupload, name='newupload'),
    path('bidding', views.bid, name='bid'),
    path('checkout', views.checkout, name='checkout'),
    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
