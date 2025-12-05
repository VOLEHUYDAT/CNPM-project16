from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from sympy import n_order
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
    path('contact/', views.contact, name="contact"),
    path('advertise/', views.advertise, name="advertise"),
    path('payment_success/', views.payment_success, name="payment_success"),
    path('apply_voucher/', views.apply_voucher, name='apply_voucher'),

    path('pay',views.index, name='index'),
    path('payment',views.payment, name='payment'),
    path('payment_ipn',views.payment_ipn, name='payment_ipn'),
    path('payment_return',views.payment_return, name='payment_return'),
    path('query', views.query, name='query'),
    path('refund', views.refund, name='refund'),
    path('submit_review/<int:product_id>/', views.submit_review, name='submit_review'),
    #path('admin/', admin.site.urls),
    path(
        'password_reset/',
        auth_views.PasswordResetView.as_view(
            template_name='app/password_reset_form.html',
            email_template_name='app/password_reset_email.txt',          # plain text
            html_email_template_name='app/password_reset_email.html',    # HTML (quan trọng)
            subject_template_name='app/password_reset_subject.txt',
            success_url=reverse_lazy('password_reset_done'),
        ),
        name='password_reset',
    ),
    path(
        'password_reset/done/',
        auth_views.PasswordResetDoneView.as_view(
            template_name='app/password_reset_done.html',
        ),
        name='password_reset_done',
    ),
    path(
        'reset/<uidb64>/<token>/',
        auth_views.PasswordResetConfirmView.as_view(
            template_name='app/password_reset_confirm.html',
            success_url=reverse_lazy('password_reset_complete'),
        ),
        name='password_reset_confirm',
    ),
    path(
        'reset/done/',
        auth_views.PasswordResetCompleteView.as_view(
            template_name='app/password_reset_complete.html',
        ),
        name='password_reset_complete',
    ),
    path('chat/', views.chat_page, name='chat'),
    path('send_message/', views.send_message, name='send_message'),
    path('load_messages/', views.load_messages, name='load_messages'),
    path('admin_chat/', views.admin_chat_page, name='admin_chat'),

    path('order-history/', views.order_history, name='order_history'),
    path('order-detail/<int:order_id>/', views.order_detail, name='order_detail'),

    path('sales-report/', views.sales_dashboard, name='sales_dashboard'),

    path("my-orders/", views.my_orders, name="my_orders"),
    path("<int:order_id>/received/", views.confirm_received, name="confirm_received"),

    path("manage-orders/", views.admin_manage_orders, name="admin_manage_orders"),
    path('update-status/<int:order_id>/', views.admin_update_status_single, name='admin_update_status_single'),

]
