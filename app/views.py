from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.http import JsonResponse
from .models import *
import json
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

from django.core.mail import send_mail
from django.views.decorators.csrf import csrf_exempt
from django.utils.timezone import now
import hashlib
import hmac
import json
import urllib
from urllib.parse import quote
import urllib.request
import random
import requests # type: ignore
from datetime import datetime
from django.conf import settings
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login

from app.models import PaymentForm
from app.vnpay import vnpay
from .formss import ReviewForm
# Create your views here.
def advertise(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub =False)
    context={'items':items,'order':order,'cartItems':cartItems,'categories':categories}
    return render(request,'app/advertise.html', context)
def detail(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    id = request.GET.get('id','')
    products = Product.objects.filter(id=id)
    reviews = ReviewRating.objects.filter(product_id__in=products.values_list('id', flat=True), status=True)
    categories = Category.objects.filter(is_sub =False)
    context={'products':products, 'items':items,'order':order,'cartItems':cartItems,'categories':categories,'reviews': reviews}
    return render(request, 'app/detail.html', context)
def category(request):
    categories = Category.objects.filter(is_sub =False)
    active_category = request.GET.get('category','')
    if active_category:
        products = Product.objects.filter(category__slug = active_category)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
       
    else:
        items =[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    
    context = {'categories': categories, 'products': products, 'active_category': active_category, 'cartItems':cartItems}
    return render(request,'app/category.html',context)
def search(request):
    if request.method =="POST":
        searched = request.POST["searched"]
        keys = Product.objects.filter(name__contains =searched)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
       
    else:
        items =[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub =False)
    products = Product.objects.all()
    return render(request,'app/search.html',{"searched":searched,"keys":keys,'products':products, 'cartItems':cartItems, 'categories': categories})

def register(request):
    form = CreateUserForm()  
    if request.method =="POST":
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    context ={'form': form}
    return render(request,'app/register.html', context)
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    if request.method =="POST":
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request,username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else: messages.info(request,'user or password not correct')
    context ={}
    return render(request,'app/login.html', context)
def logoutPage(request):
    logout(request)
    return redirect('login')
def home(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        order = None
        items = []
        cartItems = 0

    categories = Category.objects.filter(is_sub=False)
    products = Product.objects.all()

    context = {
        'products': products,
        'cartItems': cartItems,
        'categories': categories,
        'order': order
    }
    return render(request, 'app/home.html', context)
def cart(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items']
    categories = Category.objects.filter(is_sub =False)
    context={'items':items,'order':order,'cartItems':cartItems,'categories':categories}
    return render(request, 'app/cart.html', context)
# File: CNPM-project16/app/views.py - HÀM checkout(request) ĐÃ SỬA

def checkout(request):
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items

        # Lấy address duy nhất theo Order
        existing_shipping = ShippingAddress.objects.filter(order=order).first()

        discount_amount = order.discount_amount if order.voucher else 0
        total_after_discount = order.get_cart_total - discount_amount

        if request.method == 'POST':
            name = request.POST.get('name')
            email = request.POST.get('email')
            address = request.POST.get('address')
            city = request.POST.get('city')
            state = request.POST.get('state')
            mobile = request.POST.get('mobile')
            country = request.POST.get('country')

            if not name or not email or not address or not city or not state or not mobile or not country:
                messages.error(request, "Please fill in all required fields.")
                return redirect('checkout')

            # Luôn chỉ có 1 địa chỉ cho 1 Order
            ShippingAddress.objects.update_or_create(
                order=order,
                defaults={
                    'customer': customer,
                    'address': address,
                    'city': city,
                    'state': state,
                    'mobile': mobile,
                }
            )

            messages.success(request, "Shipping address saved successfully!")
            return redirect('payment')

    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = order['get_cart_items']
        discount_amount = 0
        total_after_discount = 0
        existing_shipping = None

    categories = Category.objects.filter(is_sub=False)

    context = {
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'categories': categories,
        'discount_amount': discount_amount,
        'total_after_discount': total_after_discount,
        'shipping_address': existing_shipping
    }

    return render(request, 'app/checkout.html', context)

def updateItem(request):
    data = json.loads(request.body)
    productId = data['productId']
    action = data['action']
    customer = request.user
    product = Product.objects.get(id = productId)
    # --- CHECK HẾT HÀNG ---
    if action == 'add' and product.stock <= 0:
        return JsonResponse({'error': 'Hết hàng'}, status=400)
    # -----------------------

    order, created = Order.objects.get_or_create(customer=customer, complete=False)
    orderItem, created = OrderItem.objects.get_or_create(order=order, product=product)

    # tăng / giảm số lượng
    if action == 'add':
        orderItem.quantity += 1
        product.stock -= 1     # trừ kho
        product.save()
    elif action == 'remove':
        orderItem.quantity -= 1
        product.stock += 1     # trả lại kho
        product.save()

    orderItem.save()
    if orderItem.quantity <=0:
        orderItem.delete()
    return JsonResponse('added',safe=False)





def index(request):
    return render(request, "payment/index.html", {"title": "Danh sách "})


def hmacsha512(key, data):
    byteKey = key.encode('utf-8')
    byteData = data.encode('utf-8')
    return hmac.new(byteKey, byteData, hashlib.sha512).hexdigest()


def payment(request):

    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer = customer, complete = False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items =[]
        order={'get_cart_items':0,'get_cart_total':0}
        cartItems = order['get_cart_items'] 

    discount_amount = order.discount_amount if hasattr(order, 'discount_amount') else 0
    total_after_discount = max(order.get_cart_total - discount_amount, 0)  # Không để số âm
    

    if request.method == 'POST':
        # Process input data and build url payment
        form = PaymentForm(request.POST)
        if form.is_valid():
            order_type = form.cleaned_data['order_type']
            order_id = form.cleaned_data['order_id']
            amount = form.cleaned_data['amount']
            order_desc = form.cleaned_data['order_desc']
            bank_code = form.cleaned_data['bank_code']
            language = form.cleaned_data['language']
            ipaddr = get_client_ip(request)
            # Build URL Payment
            vnp = vnpay()
            vnp.requestData['vnp_Version'] = '2.1.0'
            vnp.requestData['vnp_Command'] = 'pay'
            vnp.requestData['vnp_TmnCode'] = settings.VNPAY_TMN_CODE
            vnp.requestData['vnp_Amount'] = amount * 100
            vnp.requestData['vnp_CurrCode'] = 'VND'
            vnp.requestData['vnp_TxnRef'] = order_id
            vnp.requestData['vnp_OrderInfo'] = order_desc
            vnp.requestData['vnp_OrderType'] = order_type
            # Check language, default: vn
            if language and language != '':
                vnp.requestData['vnp_Locale'] = language
            else:
                vnp.requestData['vnp_Locale'] = 'vn'
                # Check bank_code, if bank_code is empty, customer will be selected bank on VNPAY
            if bank_code and bank_code != "":
                vnp.requestData['vnp_BankCode'] = bank_code

            vnp.requestData['vnp_CreateDate'] = datetime.now().strftime('%Y%m%d%H%M%S')  # 20150410063022
            vnp.requestData['vnp_IpAddr'] = ipaddr
            vnp.requestData['vnp_ReturnUrl'] = settings.VNPAY_RETURN_URL
            vnpay_payment_url = vnp.get_payment_url(settings.VNPAY_PAYMENT_URL, settings.VNPAY_HASH_SECRET_KEY)
            print(vnpay_payment_url)
            return redirect(vnpay_payment_url)
        else:
            print("Form input not validate")
    else:
        context={'items':items,'order':order,'cartItems':cartItems,'discount_amount':discount_amount,'total_after_discount':total_after_discount,'title': "Thanh toán"}
        return render(request, "payment/payment.html",context )

def payment_ipn(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = inputData['vnp_Amount']
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']
        vnp_TmnCode = inputData['vnp_TmnCode']
        vnp_PayDate = inputData['vnp_PayDate']
        vnp_BankCode = inputData['vnp_BankCode']
        vnp_CardType = inputData['vnp_CardType']
        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            # Check & Update Order Status in your Database
            # Your code here
            firstTimeUpdate = True
            totalamount = True
            if totalamount:
                if firstTimeUpdate:
                    if vnp_ResponseCode == '00':
                        print('Payment Success. Your code implement here')
                    else:
                        print('Payment Error. Your code implement here')

                    # Return VNPAY: Merchant update success
                    result = JsonResponse({'RspCode': '00', 'Message': 'Confirm Success'})
                else:
                    # Already Update
                    result = JsonResponse({'RspCode': '02', 'Message': 'Order Already Update'})
            else:
                # invalid amount
                result = JsonResponse({'RspCode': '04', 'Message': 'invalid amount'})
        else:
            # Invalid Signature
            result = JsonResponse({'RspCode': '97', 'Message': 'Invalid Signature'})
    else:
        result = JsonResponse({'RspCode': '99', 'Message': 'Invalid request'})

    return result


def payment_return(request):
    inputData = request.GET
    if inputData:
        vnp = vnpay()
        vnp.responseData = inputData.dict()
        order_id = inputData['vnp_TxnRef']
        amount = int(inputData['vnp_Amount']) / 100
        order_desc = inputData['vnp_OrderInfo']
        vnp_TransactionNo = inputData['vnp_TransactionNo']
        vnp_ResponseCode = inputData['vnp_ResponseCode']

        # Lưu log thanh toán
        Payment_VNPay.objects.create(
            order_id=order_id,
            amount=amount,
            order_desc=order_desc,
            vnp_TransactionNo=vnp_TransactionNo,
            vnp_ResponseCode=vnp_ResponseCode
        )

        if vnp.validate_response(settings.VNPAY_HASH_SECRET_KEY):
            if vnp_ResponseCode == "00":
                if request.user.is_authenticated:
                    # Lấy đơn hàng hiện tại (status: complete=False)
                    order = Order.objects.filter(customer=request.user, complete=False).first()
                    if order:
                        # Đánh dấu đơn đã hoàn tất
                        order.complete = True
                        order.save()

                        # Tạo giỏ hàng mới cho user (trống)
                        Order.objects.create(customer=request.user, complete=False)

                    # Gửi email
                    subject = f'Thanh toán hóa đơn {order_id} thành công'
                    body = (
                        f'Mã hóa đơn: {order_id}\n'
                        f'Số tiền: {amount}\n'
                        f'Nội dung thanh toán: {order_desc}'
                    )
                    send_mail(subject, body, 'huydat13825@gmail.com', [request.user.email])

                return render(request, "payment/payment_return.html", {
                    "title": "Kết quả thanh toán",
                    "result": "Thành công",
                    "order_id": order_id,
                    "amount": amount,
                    "order_desc": order_desc,
                    "vnp_TransactionNo": vnp_TransactionNo,
                    "vnp_ResponseCode": vnp_ResponseCode
                })

            # ❌ Thanh toán thất bại
            else:
                return render(request, "payment/payment_return.html", {
                    "title": "Kết quả thanh toán",
                    "result": "Lỗi",
                    "order_id": order_id,
                    "amount": amount,
                    "order_desc": order_desc,
                    "vnp_TransactionNo": vnp_TransactionNo,
                    "vnp_ResponseCode": vnp_ResponseCode
                })

        # Sai checksum
        return render(request, "payment/payment_return.html", {
            "title": "Kết quả thanh toán",
            "result": "Lỗi - Sai checksum"
        })

    # Không có input đầu vào
    return render(request, "payment/payment_return.html", {
        "title": "Kết quả thanh toán",
        "result": ""
    })





def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

n = random.randint(10**11, 10**12 - 1)
n_str = str(n)
while len(n_str) < 12:
    n_str = '0' + n_str


def query(request):
    if request.method == 'GET':
        return render(request, "payment/query.html", {"title": "Kiểm tra kết quả giao dịch"})

    url = settings.VNPAY_API_URL
    secret_key = settings.VNPAY_HASH_SECRET_KEY
    vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnp_Version = '2.1.0'

    vnp_RequestId = n_str
    vnp_Command = 'querydr'
    vnp_TxnRef = request.POST['order_id']
    vnp_OrderInfo = 'kiem tra gd'
    vnp_TransactionDate = request.POST['trans_date']
    vnp_CreateDate = datetime.now().strftime('%Y%m%d%H%M%S')
    vnp_IpAddr = get_client_ip(request)

    hash_data = "|".join([
        vnp_RequestId, vnp_Version, vnp_Command, vnp_TmnCode,
        vnp_TxnRef, vnp_TransactionDate, vnp_CreateDate,
        vnp_IpAddr, vnp_OrderInfo
    ])

    secure_hash = hmac.new(secret_key.encode(), hash_data.encode(), hashlib.sha512).hexdigest()

    data = {
        "vnp_RequestId": vnp_RequestId,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_Command": vnp_Command,
        "vnp_TxnRef": vnp_TxnRef,
        "vnp_OrderInfo": vnp_OrderInfo,
        "vnp_TransactionDate": vnp_TransactionDate,
        "vnp_CreateDate": vnp_CreateDate,
        "vnp_IpAddr": vnp_IpAddr,
        "vnp_Version": vnp_Version,
        "vnp_SecureHash": secure_hash
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = json.loads(response.text)
    else:
        response_json = {"error": f"Request failed with status code: {response.status_code}"}

    return render(request, "payment/query.html", {"title": "Kiểm tra kết quả giao dịch", "response_json": response_json})

def refund(request):
    if request.method == 'GET':
        return render(request, "payment/refund.html", {"title": "Hoàn tiền giao dịch"})

    url = settings.VNPAY_API_URL
    secret_key = settings.VNPAY_HASH_SECRET_KEY
    vnp_TmnCode = settings.VNPAY_TMN_CODE
    vnp_RequestId = n_str
    vnp_Version = '2.1.0'
    vnp_Command = 'refund'
    vnp_TransactionType = request.POST['TransactionType']
    vnp_TxnRef = request.POST['order_id']
    vnp_Amount = request.POST['amount']
    vnp_OrderInfo = request.POST['order_desc']
    vnp_TransactionNo = '0'
    vnp_TransactionDate = request.POST['trans_date']
    vnp_CreateDate = datetime.now().strftime('%Y%m%d%H%M%S')
    vnp_CreateBy = 'user01'
    vnp_IpAddr = get_client_ip(request)

    hash_data = "|".join([
        vnp_RequestId, vnp_Version, vnp_Command, vnp_TmnCode, vnp_TransactionType, vnp_TxnRef,
        vnp_Amount, vnp_TransactionNo, vnp_TransactionDate, vnp_CreateBy, vnp_CreateDate,
        vnp_IpAddr, vnp_OrderInfo
    ])

    secure_hash = hmac.new(secret_key.encode(), hash_data.encode(), hashlib.sha512).hexdigest()

    data = {
        "vnp_RequestId": vnp_RequestId,
        "vnp_TmnCode": vnp_TmnCode,
        "vnp_Command": vnp_Command,
        "vnp_TxnRef": vnp_TxnRef,
        "vnp_Amount": vnp_Amount,
        "vnp_OrderInfo": vnp_OrderInfo,
        "vnp_TransactionDate": vnp_TransactionDate,
        "vnp_CreateDate": vnp_CreateDate,
        "vnp_IpAddr": vnp_IpAddr,
        "vnp_TransactionType": vnp_TransactionType,
        "vnp_TransactionNo": vnp_TransactionNo,
        "vnp_CreateBy": vnp_CreateBy,
        "vnp_Version": vnp_Version,
        "vnp_SecureHash": secure_hash
    }

    headers = {"Content-Type": "application/json"}

    response = requests.post(url, headers=headers, data=json.dumps(data))

    if response.status_code == 200:
        response_json = json.loads(response.text)
    else:
        response_json = {"error": f"Request failed with status code: {response.status_code}"}

    return render(request, "payment/refund.html", {"title": "Kết quả hoàn tiền giao dịch", "response_json": response_json})


def payment_success(request):
    if request.method == 'POST':
        vnp_ResponseCode = request.POST.get('vnp_ResponseCode')

        if vnp_ResponseCode == '00':
            if request.user.is_authenticated:
                order = Order.objects.filter(customer=request.user, complete=False).first()
            return redirect('home') 
        else:
            messages.error(request, "Thanh toán không thành công.")
            return redirect('cart')  
    else:
        messages.error(request, "Yêu cầu không hợp lệ.")
        return redirect('cart') 



@csrf_exempt  
def contact(request):
    if request.method == 'POST':
        
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        recipient_list = [request.POST.get('email')]

       
        try:
            send_mail(subject, message, 'huydat13825@gmail.com', recipient_list)
            messages.success(request, 'Email đã được gửi thành công!')
        except Exception as e:
            messages.error(request, f'Có lỗi xảy ra: {e}')
        
        
        return redirect('home')  

    return render(request, 'app/contact.html')

def submit_review(request, product_id):
    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        try:
            reviews = ReviewRating.objects.get(user__id=request.user.id, product__id=product_id)
            form = ReviewForm(request.POST, instance=reviews)
            form.save()
            messages.success(request, 'Thank you! Your review has been updated.')
            return redirect(url)
        except ReviewRating.DoesNotExist:
            form = ReviewForm(request.POST)
            if form.is_valid():
                data = ReviewRating()
                data.subject = form.cleaned_data['subject']
                data.rating = form.cleaned_data['rating']
                data.review = form.cleaned_data['review']
                data.ip = request.META.get('REMOTE_ADDR')
                data.product_id = product_id
                data.user_id = request.user.id
                data.save()
                messages.success(request, 'Thank you! Your review has been submitted.')
                return redirect(url)

#them ma voucher
def apply_voucher(request):
    if request.method == 'POST':
        voucher_code = request.POST.get('voucher_code')
        voucher = Voucher.objects.filter(code=voucher_code, status=True).first()

        if not voucher:
            messages.error(request, "Invalid or expired voucher.")
            return redirect('cart')

        order = Order.objects.get(customer=request.user, complete=False)

        # Kiểm tra nếu đơn hàng đủ điều kiện để sử dụng voucher
        if order.get_cart_total < voucher.min_purchase_amount:
            messages.error(request, "Order total is too low to use this voucher.")
            return redirect('cart')

        if voucher.expiration_date < now():
            messages.error(request, "This voucher has expired.")
            return redirect('cart')

        # Tính toán số tiền giảm giá từ voucher
        discount_amount = (voucher.discount_percentage / 100) * order.get_cart_total

        # Lưu voucher vào đơn hàng và cập nhật số tiền giảm giá
        order.voucher = voucher
        order.discount_amount = int(discount_amount)  # 🛠 Chuyển về số nguyên
        order.save()

        messages.success(request, f"Voucher applied! You saved {order.discount_amount} VNĐ.")

    return redirect('cart')

@login_required
def order_history(request):
    """Hiển thị danh sách các đơn hàng đã hoàn tất của người dùng."""
    customer = request.user
    # Lấy TẤT CẢ các đơn hàng ĐÃ HOÀN TẤT (complete=True) và sắp xếp theo ngày mới nhất
    orders = Order.objects.filter(customer=customer, complete=True).order_by('-date_ordered')
    
    context = {
        'orders': orders,
        'title': 'Lịch sử Đơn hàng'
    }
    return render(request, 'app/order_history.html', context)
from django.shortcuts import render, redirect, get_object_or_404
@login_required
def order_detail(request, order_id):
    """Hiển thị chi tiết một đơn hàng cụ thể."""
    # Dùng get_object_or_404 để trả về lỗi 404 nếu không tìm thấy đơn hàng
    order = get_object_or_404(Order, id=order_id, customer=request.user)
    
    # Lấy tất cả OrderItem (sản phẩm) thuộc về đơn hàng này
    items = order.orderitem_set.all()
    
    context = {
        'order': order,
        'items': items,
        'title': f'Chi tiết Đơn hàng #{order.id}'
    }
    return render(request, 'app/order_detail.html', context)

from django.db.models import Sum
from django.db.models.functions import ExtractMonth, ExtractYear
import json
from django.contrib.auth.decorators import login_required
from django.core.serializers.json import DjangoJSONEncoder
from django.db.models import F

# ... (các hàm view khác) ...

@login_required
def sales_dashboard(request):
    """Hiển thị dashboard thống kê số lượng sản phẩm bán ra theo tháng."""

    # Lấy dữ liệu bán hàng theo từng tháng + năm
    sales_data_query = (
        OrderItem.objects.filter(order__complete=True)
        .annotate(
            month_num=ExtractMonth('order__date_order'),
            year_num=ExtractYear('order__date_order')
        )
        .values(
            'month_num',
            'year_num',
            product_name=F('product__name')
        )
        .annotate(total_quantity=Sum('quantity'))
        .order_by('year_num', 'month_num')
    )

    # Chuyển QuerySet → JSON để gửi sang frontend
    sales_data_list = list(sales_data_query)
    sales_data_json = json.dumps(sales_data_list, cls=DjangoJSONEncoder)

    # Lấy thông tin giỏ hàng
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = 0

    categories = Category.objects.filter(is_sub=False)

    # Danh sách tháng / năm để user lựa chọn
    current_year = datetime.now().year

    context = {
        'title': 'Báo Cáo Thống Kê Bán Hàng',
        'categories': categories,
        'items': items,
        'cartItems': cartItems,
        'order': order,

        # Dữ liệu Chart.js
        'sales_data_json': sales_data_json,

        # Dữ liệu lọc
        'months': range(1, 13),
        'years': range(2020, current_year + 1),
    }

    return render(request, 'app/sales_dashboard.html', context)

from django.http import JsonResponse
from django.contrib.auth.decorators import login_required
from .models import ChatMessage, User

@login_required
def chat_page(request):
    admin_user = User.objects.get(username="admin")
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = 0

    categories = Category.objects.filter(is_sub=False)
    context={
            'items':items,
             'order':order,
             'cartItems':cartItems,
             'categories':categories,
             "admin": admin_user
            }
    return render(request, "app/chat.html", context)

@login_required
def send_message(request):
    if request.method == "POST":
        msg = request.POST.get("message")
        admin_user = User.objects.get(username="admin")
        ChatMessage.objects.create(
            sender=request.user,
            receiver=admin_user,
            message=msg
        )
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"})

@login_required
def load_messages(request):
    """
    Nếu admin load, cần truyền user_id để xem chat với khách hàng nào
    """
    if request.user.username == "admin":
        user_id = request.GET.get("user_id")
        if not user_id:
            return JsonResponse([], safe=False)
        other_user = User.objects.get(id=user_id)
        messages = ChatMessage.objects.filter(
            sender__in=[other_user, request.user],
            receiver__in=[other_user, request.user]
        ).order_by("timestamp")
    else:
        admin_user = User.objects.get(username="admin")
        messages = ChatMessage.objects.filter(
            sender__in=[request.user, admin_user],
            receiver__in=[request.user, admin_user]
        ).order_by("timestamp")

    data = [
        {
            "sender": msg.sender.username,
            "message": msg.message,
            "time": msg.timestamp.strftime("%H:%M %d-%m")
        }
        for msg in messages
    ]
    return JsonResponse(data, safe=False)

@login_required
def admin_chat_page(request):
    if not request.user.is_staff:
        return redirect("home")

    users = User.objects.exclude(username="admin")

    # xử lý giỏ hàng
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = 0

    categories = Category.objects.filter(is_sub=False)

    context = {
        'users': users,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'categories': categories,
    }

    return render(request, "app/admin_chat.html", context)

from django.contrib.admin.views.decorators import staff_member_required

@staff_member_required
def admin_manage_orders(request):
    orders = Order.objects.all().order_by('-id')

    if request.method == "POST":
        for order in orders:
            new_status = request.POST.get(f"status_{order.id}")
            if new_status:
                order.status = new_status
                order.save()
        return redirect('admin_manage_orders')

    return render(request, "app/admin_manage_orders.html", {"orders": orders})


@login_required
def my_orders(request):
    orders = Order.objects.filter(customer=request.user)
    if request.user.is_authenticated:
        customer = request.user
        order, created = Order.objects.get_or_create(customer=customer, complete=False)
        items = order.orderitem_set.all()
        cartItems = order.get_cart_items
    else:
        items = []
        order = {'get_cart_items': 0, 'get_cart_total': 0}
        cartItems = 0

    categories = Category.objects.filter(is_sub=False)

    context = {
        'orders': orders,
        'items': items,
        'order': order,
        'cartItems': cartItems,
        'categories': categories,
    }

    return render(request, "app/user_orders.html", context)

@login_required
def confirm_received(request, order_id):
    order = Order.objects.get(id=order_id, customer=request.user)

    if order.status == 'delivered':
        order.status = 'completed'
        order.save()
    return redirect('my_orders')

@staff_member_required
def admin_update_status_single(request, order_id):
    order = Order.objects.get(id=order_id)
    if request.method == "POST":
        order.status = request.POST.get("status")
        order.save()
    return redirect('admin_manage_orders')

