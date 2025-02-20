from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django import forms
#Category
class Category(models.Model):
    sub_category = models.ForeignKey('self', on_delete=models.CASCADE, related_name= 'sub_categories', null=True, blank=True)
    is_sub = models.BooleanField(default=False)
    name = models.CharField(max_length=200, null=True)
    slug = models.SlugField(max_length=200,unique=True)
    def __str__(self):
        return self.name
#change forms register
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email','first_name','last_name','password1','password2']
# Create your models here.


class Product(models.Model):
    category = models.ManyToManyField(Category, related_name='product')
    name = models.CharField(max_length=200,null=True,blank=False)
    price = models.BigIntegerField()
    media = models.ImageField(null=True,blank=True)
    detail = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name 
    @property
    def ImageURL(self):
        try:
            url = self.media.url
        except:
            url=''
        return url

#them ma voucher
class Voucher(models.Model):
    code = models.CharField(max_length=50, unique=True)
    discount_percentage = models.FloatField(default=0)  # Giảm theo phần trăm
    discount_amount = models.IntegerField(default=0)  # Giảm giá cố định theo số tiền
    min_purchase_amount = models.IntegerField(default=0)  # Số tiền tối thiểu để áp dụng voucher
    expiration_date = models.DateTimeField()
    status = models.BooleanField(default=True)  # Trạng thái voucher (còn hoạt động không)

    def __str__(self):
        return f"{self.code} - {self.discount_amount} VNĐ"

class Order(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    date_order = models.DateTimeField(auto_now_add=True)
    name = models.CharField(max_length=200,null=True,blank=False)
    complete = models.BooleanField(default=False,null=True,blank=False)
    transaction_id = models.CharField(max_length=200,null=True)

    #mã voucher
    voucher = models.ForeignKey(Voucher, on_delete=models.SET_NULL, blank=True, null=True)
    discount_amount = models.FloatField(default=0)  # 🛠 Lưu số tiền giảm giá

    def __str__(self):
        return str(self.id)
    @property
    def get_cart_items(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.quantity for item in orderitems])
        return total
    @property
    def get_cart_total(self):
        orderitems = self.orderitem_set.all()
        total = sum([item.get_total for item in orderitems])
        return total


class OrderItem(models.Model):
    product = models.ForeignKey(Product,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    quantity = models.IntegerField(default=0,null=True,blank=True)
    date_added = models.DateTimeField(auto_now_add=True)
    @property
    def get_total(self):
        total = self.product.price * self.quantity
        return total

class ShippingAddress(models.Model):
    customer = models.ForeignKey(User,on_delete=models.SET_NULL,blank=True,null=True)
    order = models.ForeignKey(Order,on_delete=models.SET_NULL,blank=True,null=True)
    address = models.CharField(max_length=200,null=True)
    city = models.CharField(max_length=200,null=True)
    state = models.CharField(max_length=200,null=True)
    mobile = models.CharField(max_length=10,null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.address
class PaymentForm(forms.Form):

    order_id = forms.CharField(max_length=250)
    order_type = forms.CharField(max_length=20)
    amount = forms.IntegerField()
    order_desc = forms.CharField(max_length=100)
    bank_code = forms.CharField(max_length=20, required=False)
    language = forms.CharField(max_length=2)

class Payment_VNPay(models.Model):
    order_id = models.BigIntegerField(default=0, null=True, blank=True)
    amount = models.BigIntegerField(default=0, null=True, blank=True)
    order_desc = models.CharField(max_length=200,null=True,blank=True)
    vnp_TransactionNo = models.CharField(max_length=200,null=True,blank=True)
    vnp_ResponseCode = models.CharField(max_length=200, null=True, blank=True)

class ReviewRating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    subject = models.CharField(max_length=100, blank=True)
    review = models.TextField(max_length=500, blank=True)
    rating = models.FloatField()
    ip = models.CharField(max_length=20, blank=True)
    status = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject



