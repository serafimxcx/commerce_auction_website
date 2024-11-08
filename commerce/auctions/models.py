from django.contrib.auth.models import AbstractUser
from django.db import models
from datetime import datetime
from django.db.models import Max



class User(AbstractUser):
    pass

class Category(models.Model):
    name = models.CharField(max_length=255)

    def __str__ (self):
        return f"{self.name}"

class AuctionItem(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255)
    price = models.DecimalField(max_digits=11, decimal_places=2)
    description = models.CharField(max_length=500)
    image = models.ImageField(upload_to='items/', null=True)
    date = models.DateField(auto_now_add=True)
    time = models.TimeField(auto_now_add=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    isOpen = models.BooleanField(default=True)

    def __str__ (self):
        return f"{self.category} : {self.name}"
    
    def latest_bid(self):
        latest_bid = self.bid_set.aggregate(latest_bid=Max('bid'))
        return latest_bid['latest_bid'] if latest_bid['latest_bid'] is not None else self.price

class Watchlist(models.Model):
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user} : {self.item}"

class Bid(models.Model):
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    bid = models.DecimalField(max_digits=11, decimal_places=2)
    datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user} : {self.item} : {self.bid}"
    
class Comment(models.Model):
    item = models.ForeignKey(AuctionItem, on_delete=models.CASCADE, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    content = models.TextField(max_length=500)
    datetime = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"{self.user} : {self.item}"

