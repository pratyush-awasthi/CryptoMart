# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from random import sample, choices
from unicodedata import category
from django.contrib import messages
from django import template
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.template import loader
from django.urls import reverse
from requests import session
import stripe
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt
from sympy import Id, re
from .forms import *
from .models import *
from django.shortcuts import render, redirect, get_object_or_404
from uuid import uuid4


@login_required(login_url="/login/")
def index(request):
    context = {'segment': 'index'}

    html_template = loader.get_template('home/index.html')
    return HttpResponse(html_template.render(context, request))


@csrf_exempt
def stripe_config(request):
    if request.method == "GET":
        stripe_config = {'publicKey': settings.STRIPE_PUBLISHABLE_KEY}
        return JsonResponse(stripe_config, safe=False)


@csrf_exempt
def create_checkout_session(request):
    if request.method == 'GET':
        domain_url = "http://127.0.0.1:8000/"
        stripe.api_key = settings.STRIPE_SECRET_KEY
        price = request.GET.get('price')
        pid = request.GET.get('pid')
        item = Nft.objects.filter(id=pid).first()

        price = str(price).replace('.', '0')+"00"
        print("price", price, "item", item)
        itemdata = [{
            'name': item.title,
                    'quantity': 1,
                    'currency': 'inr',
                    'amount': int(price),
                    'description': item.description,
                    }]

        try:
            checkout_session = stripe.checkout.Session.create(
                # new
                client_reference_id=request.user.id if request.user.is_authenticated else None,
                success_url=domain_url + \
                'success?session_id={CHECKOUT_SESSION_ID}',
                cancel_url=domain_url + 'cancelled/',
                payment_method_types=['card'],
                mode='payment',
                line_items=itemdata,
            )
            owner = User.objects.filter(
                username__icontains=item.owner.split()[0]).first()
            print(item.owner, owner)
            order = Transaction(
                transaction_id=checkout_session['id'],
                old_owner=owner,
                new_owner=request.user,
                details=item.title+" purchased",
                nft=item,
                deposit_address=uuid4())
            order.save()
            request.session['orderId'] = order.id
            return JsonResponse({'sessionId': checkout_session['id']})
        except Exception as e:
            print(e)
            return JsonResponse({'error': str(e)})


def notify_success(request):
    messages.success(request, f"Your payment is complete.")
    if 'orderId' in request.session:
        order = Transaction.objects.get(id=request.session['orderId'])
        ctx = {
            'title': 'Successful',
            'order': order
        }
        return render(request, "home/success.html", ctx)
    return render(request, "home/success.html")


def notify_cancelled(request):
     
    messages.error(request, f"Your payment is cancelled.")
    ctx = {
            'title': 'Cancelled',
        }
    return render(request, "home/cancelled.html",ctx)


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
           'feed': feed}
    return render(request, "home/viewfeedback.html", ctx)


def allnfts(request):
    categories = Category.objects.all()
    nfts = Nft.objects.all()
    ctx = {'title': "All Nfts",
           'nfts': nfts,
           'cats': categories,
           }
    return render(request, "home/allnfts.html", ctx)


def landing(request):
    categories = Category.objects.all()
    nfts = choices(list(Nft.objects.filter(
        category__name__contains='Collectibles')), k=12)
    artnfts = choices(list(Nft.objects.filter(
        category__name__contains='Art')), k=8)
    trans = Transaction.objects.all()
    print(len(nfts))
    print(len(artnfts))
    ctx = {'title': "Home",
           'nfts': nfts,
           'artnfts': artnfts,
           'cats': categories,
           'trans': trans,
           }
    return render(request, "home/landing.html", ctx)


@login_required(login_url="/login/")
def newupload(request):
    context = {'segment': 'newupload'}
    form = NftForm()
    if request.method == 'POST':
        form = NftForm(request.POST, request.FILES)
        if form.is_valid():
            logo = form.save(commit=False)
            logo.user = request.user
            logo.save()
            messages.success(request, 'Nft successfully posted.')
            return redirect('dashboard')
        else:
            messages.error(request, 'Nft could not be posted.')
    context['form'] = form
    html_template = loader.get_template('home/newupload.html')
    return render(request, 'home/newupload.html', context=context)


@login_required(login_url="/login/")
def newcategory(request):
    context = {'segment': 'newcategory'}
    form = NewCategoryForm()
    if request.method == 'POST':
        form = NewCategoryForm(request.POST, request.FILES)
        if form.is_valid():
            new = form.save(commit=False)
            new.user = request.user
            new.save()
            messages.success(request, 'New Category successfully requested.')
            return redirect('dashboard')
        else:
            messages.error(request, 'New Category could not be requested.')
    context['form'] = form
    html_template = loader.get_template('home/newcategory.html')
    return render(request, 'home/newcategory.html', context=context)


@login_required(login_url="/login/")
def feedback(request):
    context = {'segment': 'feedback'}
    form = FeedbackForm()
    if request.method == 'POST':
        form = FeedbackForm(request.POST, request.FILES)
        if form.is_valid():
            feed = form.save(commit=False)
            feed.user = request.user
            feed.save()
            messages.success(request, 'Feedback successfully posted.')
            return redirect('/')
        else:
            messages.error(request, 'Feedback could not be posted.')
    context['form'] = form
    html_template = loader.get_template('home/feedback.html')
    return render(request, 'home/feedback.html', context=context)


@login_required(login_url="/login/")
def profileedit(request):
    context = {'segment': 'Profile Edit'}
    profile = Profile.objects.filter(user=request.user).last()
    form = ProfileForm(instance=profile)
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            edit = form.save(commit=False)
            edit.user = request.user
            edit.save()
            messages.success(request, 'Profile Updated.')
            return redirect('profile')
        else:
            messages.error(request, 'Profile could not be updated.')
    context['form'] = form
    html_template = loader.get_template('home/profileedit.html')
    return render(request, 'home/profileedit.html', context=context)


def product(request, id):
    context = {
        'title': 'Product',
        'segment': 'product'
    }
    product = get_object_or_404(Nft, pk=id)
    bids = Bid.objects.filter(nft__id=id).order_by('-date')
    context['product'] = product
    context['bids'] = bids
    return render(request, 'home/product.html', context=context)


@login_required(login_url="/login/")
def checkout(request, id):
    context = {'segment': 'product'}
    product = get_object_or_404(Nft, pk=id)

    context['product'] = product
    return render(request, 'home/checkout.html', context=context)


@login_required(login_url="/login/")
def profile(request):
    profile = Profile.objects.filter(user=request.user).last()
    transactions = Transaction.objects.filter(new_owner=request.user).all()
    context = {
        'title': 'Dashboard',
        'profile': profile,
        'transactions': transactions
    }

    return render(request, 'home/profile.html', context=context)


@login_required(login_url="/login/")
def bid(request, id):
    context = {'segment': 'bid'}
    form = BidForm()
    product = get_object_or_404(Nft, pk=id)
    context['product'] = product
    if request.method == 'POST':
        form = BidForm(request.POST, request.FILES)
        if form.is_valid():
            bid = form.save(commit=False)
            bid.user = request.user
            bid.nft = product
            bid.save()
            messages.success(request, 'Bid successfully posted.')
            return redirect('product', id=id)
        else:
            messages.error(request, 'bid could not be posted.')
    context['form'] = form
    html_template = loader.get_template('home/bid.html')
    return render(request, 'home/bid.html', context=context)


def creator(request, name):
    nfts = Nft.objects.filter(creator__username__icontains=name)
    creator = Profile.objects.get(name__icontains=name)
    print(nfts)
    ctx = {'title': "Recommended Creator",
           'nfts': nfts,
           'pro': creator,
           }
    return render(request, "home/creator.html", ctx)


def search_nft(request):
    q = request.GET.get('query')
    if q:
        results = Nft.objects.filter(title__contains=q)
        print(results)
        if len(results) > 0:
            ctx = {
                'title': 'Search Results',
                'results': results,
                'query': q,
            }
            return render(request, "home/search.html", ctx)
    return redirect('landing')


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
