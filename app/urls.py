from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [

    path('', views.home, name="home"),
    path('cart/', views.cart, name="cart"),
    path('checkout/', views.checkout, name="checkout"),
    path('update_item/', views.updateItem, name="update_item"),
    path('register/', views.register, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutPage, name="logout"),
    path('search/', views.search, name="search"),
    path('category/', views.category, name="category"),
    path('detail/', views.detail, name="detail"),

    path('pay',views.index, name='index'),
    path('payment',views.payment, name='payment'),
    path('payment_ipn',views.payment_ipn, name='payment_ipn'),
    path('payment_return',views.payment_return, name='payment_return'),
    path('query', views.query, name='query'),
    path('refund', views.refund, name='refund'),
    #path('admin/', admin.site.urls),

]