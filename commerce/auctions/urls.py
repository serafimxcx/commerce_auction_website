from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("create", views.create, name="create"),
    path("categories", views.category, name="category"),
    path("item/<title>", views.item, name="item"),
    path("item/<title>/add_watchlist", views.add_watchlist, name="add_watchlist"),
    path("item/<title>/add_bid", views.add_bid, name="add_bid"),
    path("item/<title>/add_comment", views.add_comment, name="add_comment"),
    path("item/<title>/close_bidding", views.close_bidding, name="close_bidding"),
    path("watchlist", views.watchlist, name="watchlist"),
    path("remove_watchlist", views.remove_watchlist, name="remove_watchlist"),
]
