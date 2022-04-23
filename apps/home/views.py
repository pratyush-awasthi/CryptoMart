# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import messages
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.urls import reverse
from .forms import *
from .models import *
from django.shortcuts import render, redirect


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def categoryrequest(request):
    req = NewCategory.objects.all()
    ctx = {'title': "Requested Categories",
           'req': req,
           }
    return render(request, "home/categoryrequest.html", ctx)

@login_required(login_url="/login/")
def viewfeedback(request):
    feed = Feedback.objects.all()
    ctx = {'title': "All Feedbacks",
           'feed': feed,
           }
    return render(request, "home/viewfeedback.html", ctx)

def landing(request):
    nfts = Nft.objects.all()
    ctx = {'title': "Home",
           'nfts': nfts,
           }
    return render(request, "home/landing.html", ctx)

@login_required(login_url="/login/")
def newupload(request):
    context = {'segment': 'newupload'}
    form = NftForm()
    if request.method=='POST':
        form  = NftForm(request.POST, request.FILES)
        if form.is_valid():
            logo = form.save(commit=False)
            logo.user = request.user
            logo.save()
            messages.success(request,'Nft successfully posted.')
            return redirect('dashboard')
        else:
            messages.error(request,'Nft could not be posted.')
    context['form'] = form
    html_template = loader.get_template('home/newupload.html')
    return render(request,'home/newupload.html',context = context)

@login_required(login_url="/login/")
def newcategory(request):
    context = {'segment': 'newcategory'}
    form = NewCategoryForm()
    if request.method=='POST':
        form  = NewCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            logo = form.save(commit=False)
            logo.user = request.user
            logo.save()
            messages.success(request,'New Category successfully requested.')
            return redirect('dashboard')
        else:
            messages.error(request,'New Category could not be requested.')
    context['form'] = form
    html_template = loader.get_template('home/newcategory.html')
    return render(request,'home/newcategory.html',context = context)

@login_required(login_url="/login/")
def feedback(request):
    context = {'segment': 'feedback'}
    form = FeedbackForm()
    if request.method=='POST':
        form  = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            logo = form.save(commit=False)
            logo.user = request.user
            logo.save()
            messages.success(request,'Feedback successfully posted.')
            return redirect('dashboard')
        else:
            messages.error(request,'Feedback could not be posted.')
    context['form'] = form
    html_template = loader.get_template('home/feedback.html')
    return render(request,'home/feedback.html',context = context)

def product(request):
    context = {'segment': 'product'}

    html_template = loader.get_template('home/product.html')
    return HttpResponse(html_template.render(context, request))

def checkout(request):
    context = {'segment': 'checkout'}

    html_template = loader.get_template('home/checkout.html')
    return HttpResponse(html_template.render(context, request))

@login_required(login_url="/login/")
def profile(request):
    context = {'segment': 'profile'}

    html_template = loader.get_template('home/profile.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def bid(request):
    context = {'segment': 'bid'}
    form = BidForm()
    if request.method=='POST':
        form  = BidForm(request.POST, request.FILES)
        if form.is_valid():
            logo = form.save(commit=False)
            logo.user = request.user
            logo.save()
            messages.success(request,'Bid successfully posted.')
            return redirect('product')
        else:
            messages.error(request,'bid could not be posted.')
    context['form'] = form
    html_template = loader.get_template('home/bid.html')
    return render(request,'home/bid.html',context = context)

def creator(request):
    context = {'segment': 'creator'}

    html_template = loader.get_template('home/creator.html')
    return HttpResponse(html_template.render(context, request))


@login_required(login_url="/login/")
def pages(request):
    context = {}
    # All resource paths end in .html.
    # Pick out the html file name from the url. And load that template.
    try:

        load_template = request.path.split('/')[-1]

        if load_template == 'admin':
            return HttpResponseRedirect(reverse('admin:index'))
        context['segment'] = load_template

        html_template = loader.get_template('home/' + load_template)
        return HttpResponse(html_template.render(context, request))

    except template.TemplateDoesNotExist:

        html_template = loader.get_template('home/page-404.html')
        return HttpResponse(html_template.render(context, request))

    except:
        html_template = loader.get_template('home/page-500.html')
        return HttpResponse(html_template.render(context, request))
