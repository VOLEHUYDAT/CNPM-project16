from django.contrib import admin
from .models import *
# Register your models here.
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)
admin.site.register(Payment_VNPay)
admin.site.register(ReviewRating)

admin.site.register(Voucher) #mã voucher