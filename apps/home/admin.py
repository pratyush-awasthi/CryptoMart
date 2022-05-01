# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.contrib import admin
from .models import *

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    '''Admin View for Category'''

    list_display = ('name','description','created_at')
    search_fields = ('name',)

@admin.register(Currency)
class CurrencyAdmin(admin.ModelAdmin):
    '''Admin View for Currency'''

    list_display = ('name','website','short_name' ,'about')
    search_fields = ('name',)

@admin.register(Nft)
class NftAdmin(admin.ModelAdmin):
    '''Admin View for Nft'''

    list_display = ('title','price','currency','category','creator','description','owner','minted_by','mint_date','uploaded_on','on_display','is_featured','resolution','image_type','contract_address','token_id','blockchain_link')
    search_fields = ('title',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    '''Admin View for Profile'''

    list_display = ('name','bio','address','contact','wallet_id')
    search_fields = ('name',)

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    '''Admin View for Transaction'''

    list_display = ('transaction_id','deposit_address','old_owner','new_owner','details','nft','created_on')
    search_fields = ('transaction_id',)
 
@admin.register(Bid)
class BidAdmin(admin.ModelAdmin):
    '''Admin View for Bid'''

    list_display = ('nft','user','amount','date','status','deposit_address')
    search_fields = ('user',)

@admin.register(NewCategory)
class NewCategoryAdmin(admin.ModelAdmin):
    '''Admin View for NewCategory'''

    list_display = ('name','icon','email','description')
    search_fields = ('name',)
  
@admin.register(Feedback)
class FeedbackAdmin(admin.ModelAdmin):
    '''Admin View for Feedback'''
  
    list_display = ('name','subject','contact_no','email','time','description',)
    search_fields = ('name',)
   