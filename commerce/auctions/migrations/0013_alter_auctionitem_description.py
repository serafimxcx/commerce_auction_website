# Generated by Django 5.0.3 on 2024-04-07 02:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0012_rename_comment_comment_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auctionitem',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
