from django.contrib import admin
from .models import Category, AuctionItem, Watchlist, User, Bid, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(AuctionItem)
admin.site.register(Watchlist)
admin.site.register(Bid)
admin.site.register(Comment)

