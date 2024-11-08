from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from .models import Category, AuctionItem, Watchlist, Bid, Comment
from django.contrib import messages

from .models import User


def index(request):
    
    return render(request, "auctions/index.html", {
        "items": AuctionItem.objects.order_by('-isOpen', '-date', '-time'),
    })


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")

def create(request):
    if not request.user.is_authenticated:
           return HttpResponseRedirect(reverse('login'))
    else:
        user_id = request.user.id
        user = User.objects.get(pk=user_id)

        if request.method == "POST":
            selected_category_name = request.POST.get("slct_category")
            selected_category = Category.objects.get(name=selected_category_name)
            name = request.POST["txt_name"]
            price = request.POST["txt_price"]
            desc = request.POST["txt_desc"]
            image_file = request.FILES.get("upload_image", None)
            

            if image_file is not None:
                item = AuctionItem(category=selected_category, name=name, price=price, description=desc, image=image_file, author=user)
                item.save()
                return render(request, "auctions/create.html", {
                    "categories": Category.objects.all(),
                    "message": "Item Added Successfully.",
                    "items": AuctionItem.objects.filter(author=user)
                })
            else:
                return render(request, "auctions/create.html", {
                    "categories": Category.objects.all(),
                    "message": "Image not provided.",
                    "items": AuctionItem.objects.filter(author=user)
                })
        
        

        return render(request, "auctions/create.html", {
            "categories": Category.objects.all(),
            "items": AuctionItem.objects.filter(author=user)
        })

def category(request):
   
    categories = Category.objects.all()

    if request.method == "POST":
        selected_category_name = request.POST.get("slct_category")
        selected_category = Category.objects.get(name=selected_category_name)

        item = AuctionItem.objects.filter(category=selected_category).order_by('-date', '-time')
    
        return render(request, "auctions/categories.html", {
            "categories": categories,
            "selected_category": selected_category,
            "items": item
        })
    else:
        return render(request, "auctions/categories.html", {
            "categories": categories
        })

def item(request, title):
    if request.user.is_authenticated:
        item = AuctionItem.objects.filter(name=title)
        item_id = item.first().id
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        watchlist_entry = Watchlist.objects.filter(item=item_id, user=user).exists()
        comments = Comment.objects.filter(item=item_id)
        bidders = Bid.objects.filter(item=item_id).order_by('-bid')

        bid_count = Bid.objects.filter(item=item_id).count()
        bids = Bid.objects.filter(item_id=item_id)
        highest_bid = bids.order_by('-bid').first()
        bid_entry = Bid.objects.filter(item=item_id).exists()

        item_price = 0
        is_current_bid = 0
        is_current_bid = False

        if bid_entry == True:
            item_price = highest_bid.bid
        
            if highest_bid.user == user:
                is_current_bid = True
        else:
            bid_count = 0


        return render(request, "auctions/item.html", {
            "items": item,
            "watchlist_entry": watchlist_entry,
            "bid_count": bid_count,
            "item_price": item_price,
            "is_current_bid": is_current_bid,
            "comments": comments,
            "bidders": bidders,
        })
    else:
        return render(request, "auctions/login.html")        

def add_watchlist(request, title):
    if request.method == "POST":
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        item_id = request.POST.get("txt_item")
        item = AuctionItem.objects.get(pk=item_id)
        watchlist = Watchlist(item=item, user=user)

        watchlist.save()
        return HttpResponseRedirect(reverse("item", args=(title,)))
    
def watchlist(request):
    user_id = request.user.id
    user = User.objects.get(pk=user_id)
    watchlist = Watchlist.objects.filter(user=user).order_by('-datetime')
    return render(request, "auctions/watchlist.html", {
        "watchlist": watchlist
    })

def remove_watchlist(request):
    if request.method == "POST":
        watchlist_id = request.POST.get("txt_watchlist_id")
        watchlist_item = Watchlist.objects.get(pk=watchlist_id)

        watchlist_item.delete()
        return HttpResponseRedirect(reverse("watchlist"))
    
def add_bid(request, title):
    if request.method == "POST":
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        item_id = request.POST.get("txt_item")
        item_price = request.POST.get("txt_price")
        place_bid = request.POST.get("txt_bid")
        item = AuctionItem.objects.get(pk=item_id)
        bid_count = Bid.objects.filter(item=item_id).count()

        if bid_count == 0:
            if float(place_bid) < float(item_price):
                messages.success(request, 'Bid should be higher than the current bid.')
                return HttpResponseRedirect(reverse('item', args=(title,)))
            else:  
                bid = Bid(item=item, user=user, bid=place_bid)

                bid.save()
                messages.success(request, 'Bid placed successfully.')
                return HttpResponseRedirect(reverse("item", args=(title,)))
        else:
            if float(place_bid) < float(item_price) or float(place_bid) == float(item_price):
                messages.success(request, 'Bid should be higher than the current bid.')
                return HttpResponseRedirect(reverse('item', args=(title,)))
            else:  
                
                bid = Bid(item=item, user=user, bid=place_bid)

                bid.save()
                messages.success(request, 'Bid placed successfully.')
                return HttpResponseRedirect(reverse("item", args=(title,)))

def add_comment(request, title):
    if request.method == "POST":
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        item_id = request.POST.get("txt_item")
        item = AuctionItem.objects.get(pk=item_id)
        content = request.POST.get("txt_comment")

        comment = Comment(item=item, user=user, content=content)

        comment.save()
        return HttpResponseRedirect(reverse("item", args=(title,)))
    
def close_bidding(request, title):
    if request.method == "POST":
        user_id = request.user.id
        user = User.objects.get(pk=user_id)
        item_id = request.POST.get("txt_item")
        item = AuctionItem.objects.get(pk=item_id)

        item.isOpen = False

        item.save()
        return HttpResponseRedirect(reverse("item", args=(title,)))
        
