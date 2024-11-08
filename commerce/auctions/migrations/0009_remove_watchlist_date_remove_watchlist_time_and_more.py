# Generated by Django 5.0.3 on 2024-04-04 02:56

import datetime
import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0008_watchlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='watchlist',
            name='date',
        ),
        migrations.RemoveField(
            model_name='watchlist',
            name='time',
        ),
        migrations.AddField(
            model_name='watchlist',
            name='datetime',
            field=models.DateTimeField(default=datetime.datetime.now),
        ),
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bid', models.DecimalField(decimal_places=2, max_digits=11)),
                ('datetime', models.DateTimeField(default=datetime.datetime.now)),
                ('item', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='auctions.auctionitem')),
                ('user', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
