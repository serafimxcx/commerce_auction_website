# Generated by Django 5.0.3 on 2024-04-01 09:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0005_auctionitem_author_alter_auctionitem_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='watchlist',
            field=models.BooleanField(default=False),
        ),
    ]
