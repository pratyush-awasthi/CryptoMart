# Generated by Django 3.2.6 on 2022-04-09 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='icon')),
                ('description', models.TextField()),
                ('created_at', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Category',
                'verbose_name_plural': 'Categorys',
            },
        ),
        migrations.CreateModel(
            name='Currency',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('icon', models.ImageField(upload_to='currency')),
                ('website', models.URLField(max_length=255)),
                ('about', models.TextField()),
            ],
            options={
                'verbose_name': 'Currency',
                'verbose_name_plural': 'Currencys',
            },
        ),
        migrations.CreateModel(
            name='Nft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='nft')),
                ('title', models.CharField(max_length=255)),
                ('price', models.CharField(max_length=255)),
                ('description', models.TextField()),
                ('owner', models.CharField(max_length=255)),
                ('minted_by', models.CharField(max_length=255)),
                ('mint_date', models.DateTimeField(auto_now=True)),
                ('uploaded_on', models.DateTimeField()),
                ('on_display', models.BooleanField(default=False)),
                ('is_featured', models.BooleanField(default=False)),
                ('resolution', models.CharField(max_length=255)),
                ('image_type', models.CharField(choices=[('JPG', 'jpg'), ('PNG', 'png'), ('GIF', 'gif')], max_length=255)),
                ('contract_address', models.CharField(max_length=255)),
                ('token_id', models.CharField(max_length=255)),
                ('blockchain_link', models.CharField(max_length=255)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.category')),
                ('creator', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('currency', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.currency')),
            ],
            options={
                'verbose_name': 'Nft',
                'verbose_name_plural': 'Nfts',
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='profile')),
                ('name', models.CharField(max_length=255)),
                ('bio', models.TextField()),
                ('address', models.TextField()),
                ('contact', models.CharField(max_length=255)),
                ('wallet_id', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'Profile',
                'verbose_name_plural': 'Profiles',
            },
        ),
        migrations.CreateModel(
            name='Transaction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('transaction_id', models.CharField(max_length=255)),
                ('deposit_address', models.TextField()),
                ('new_owner', models.CharField(max_length=255)),
                ('details', models.TextField()),
                ('created_on', models.DateTimeField(auto_now=True)),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='home.nft')),
                ('old_owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Transaction',
                'verbose_name_plural': 'Transactions',
            },
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('amount', models.IntegerField(default=0)),
                ('date', models.DateTimeField()),
                ('status', models.BooleanField(default=False)),
                ('deposit_address', models.CharField(max_length=255)),
                ('nft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.nft')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Bid',
                'verbose_name_plural': 'Bids',
            },
        ),
    ]
