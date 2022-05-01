# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from distutils.command.upload import upload
from email.policy import default
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Currency(models.Model):
    name = models.CharField(max_length=255)
    short_name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="currency")
    website = models.URLField(max_length=255)
    about = models.TextField()
 
    class Meta:
        """Meta definition for Currency."""

        verbose_name = 'Currency'
        verbose_name_plural = 'Currencys'

    def __str__(self):
        """Unicode representation of Currency."""
        return self.name

class Category(models.Model):
    name = models.CharField(max_length=255)
    icon = models.ImageField(upload_to="icon")
    description = models.TextField()
    created_at = models.CharField(max_length=255)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Category."""

        verbose_name = 'Category'
        verbose_name_plural = 'Categorys'

    def __str__(self):
        """Unicode representation of Category."""
        return self.name

class Nft(models.Model):

    img_types = (
        ('JPG','jpg'),
        ('PNG','png'),
        ('GIF','gif')
        )

    image = models.ImageField(upload_to="nft")
    title = models.CharField(max_length=255)
    price = models.CharField(max_length=255)
    currency = models.ForeignKey(Currency,on_delete=models.CASCADE)
    category = models.ForeignKey(Category,on_delete=models.DO_NOTHING)
    creator = models.ForeignKey(User,on_delete=models.CASCADE)
    description = models.TextField()
    owner = models.CharField(max_length=255)
    minted_by = models.CharField(max_length=255)
    mint_date = models.DateTimeField(auto_now=True)
    uploaded_on = models.DateTimeField(auto_now=True)
    on_display = models.BooleanField(default=False)
    is_featured = models.BooleanField(default=False)
    resolution = models.CharField(max_length=255)
    image_type = models.CharField(max_length=255,choices=img_types)
    contract_address = models.CharField(max_length=255)
    token_id = models.CharField(max_length=255)
    blockchain_link = models.CharField(max_length=255)
    
    # TODO: Define fields here

    class Meta:
        """Meta definition for Nft."""

        verbose_name = 'Nft'
        verbose_name_plural = 'Nfts'

    def __str__(self):
        """Unicode representation of Nft."""
        return self.title

class Profile(models.Model):
    image = models.ImageField(upload_to="profile")
    banner = models.ImageField(upload_to="profile")
    name = models.CharField(max_length=255)
    bio = models.TextField()
    address = models.TextField()
    contact = models.CharField(max_length=255)
    wallet_id = models.CharField(max_length=255)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Profile."""

        verbose_name = 'Profile'
        verbose_name_plural = 'Profiles'

    def __str__(self):
        """Unicode representation of Profile."""
        return self.name

class Transaction(models.Model):
    transaction_id = models.CharField(max_length=255)
    deposit_address = models.TextField()
    old_owner = models.ForeignKey(User,on_delete=models.CASCADE)
    new_owner = models.CharField(max_length=255)
    details = models.TextField()
    nft = models.ForeignKey(Nft,on_delete=models.DO_NOTHING)
    created_on = models.DateTimeField(auto_now=True)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Transaction."""

        verbose_name = 'Transaction'
        verbose_name_plural = 'Transactions'

    def __str__(self):
        """Unicode representation of Transaction."""
        return self.transaction_id

class Bid(models.Model):
    nft = models.ForeignKey(Nft,on_delete=models.CASCADE)
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    amount = models.CharField(max_length=255)
    date = models.DateTimeField(auto_now=True)
    status = models.BooleanField(default=False)
    deposit_address = models.CharField(max_length=255)

    # TODO: Define fields here

    class Meta:
        """Meta definition for Bid."""

        verbose_name = 'Bid'
        verbose_name_plural = 'Bids'

    def __str__(self):
        """Unicode representation of Bid."""
        return self.amount

class NewCategory(models.Model):
    name = models.CharField(max_length=225)
    icon = models.ImageField(upload_to='icon')
    email = models.EmailField()
    description = models.TextField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for NewCategory."""

        verbose_name = 'NewCategory'
        verbose_name_plural = 'NewCategorys'

    def __str__(self):
        """Unicode representation of NewCategory."""
        return self.name

class Feedback(models.Model):
    name = models.CharField(max_length=225)
    subject = models.CharField(max_length=225)
    contact_no = models.CharField(max_length=225)
    email = models.EmailField()
    time = models.DateTimeField(auto_now=True)
    description = models.TextField()

    # TODO: Define fields here

    class Meta:
        """Meta definition for Feedback."""

        verbose_name = 'Feedback'
        verbose_name_plural = 'Feedbacks'

    def __str__(self):
        """Unicode representation of Feedback."""
        return self.name
