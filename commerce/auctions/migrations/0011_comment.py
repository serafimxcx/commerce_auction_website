# Generated by Django 5.0.3 on 2024-04-07 01:21

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_auctionitem_isopen'),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField(max_length=500)),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionitem')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
