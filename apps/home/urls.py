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
    path('index/', views.index, name='index'),
    path('product/<int:id>/', views.product, name='product'),
    path('creator/<str:name>', views.creator, name='creator'),
    path('profile/', views.profile, name='profile'),
    path('requested/categories/', views.categoryrequest, name='categoryrequest'),
    path('all/feedbacks/', views.viewfeedback, name='viewfeedback'),
    path('category/new/', views.newcategory, name='newcategory'),
    path('your/valuable/feedback/', views.feedback, name='feedback'),
    path('upload/new/nft/', views.newupload, name='newupload'),
    path('all/nfts/', views.allnfts, name='allnfts'),
    path('edit/your/profile/', views.profileedit, name='profileedit'),
    path('bidding/<int:id>', views.bid, name='bid'),
    path("config/",views.stripe_config, name='config'),
    path('checkout/product/buy/<int:id>/', views.checkout, name='checkout'),
    path('create-checkout-session/',views.create_checkout_session,name='create_checkout_session'),
    path('success/',views.notify_success,name='success'),
    path('cancelled/',views.notify_cancelled,name='cancelled'),
]
