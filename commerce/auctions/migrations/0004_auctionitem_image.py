# Generated by Django 5.0.3 on 2024-03-12 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auctionitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='auctionitem',
            name='image',
            field=models.ImageField(null=True, upload_to='media/items/'),
        ),
    ]
