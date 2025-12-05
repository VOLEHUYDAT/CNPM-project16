from django.contrib import admin
from .models import Product, Category, Order, OrderItem, ShippingAddress, Payment_VNPay, ReviewRating, Voucher, ChatMessage
from django.utils.html import format_html


# 1. Định nghĩa Inline cho OrderItem (Sản phẩm trong đơn hàng)
class OrderItemInline(admin.TabularInline):
    """Hiển thị các sản phẩm thuộc đơn hàng ngay trong trang chỉnh sửa Order."""
    model = OrderItem
    readonly_fields = ('product', 'quantity', 'get_total', 'date_added') 
    extra = 0 
    fields = ('product', 'quantity', 'get_total', 'date_added')

# 2. Định nghĩa Inline cho ShippingAddress (Địa chỉ giao hàng)
class ShippingAddressInline(admin.StackedInline):
    """Hiển thị địa chỉ giao hàng trong trang chỉnh sửa Order."""
    model = ShippingAddress
    max_num = 1
    extra = 0
    
    # -------------------------- FIX LỖI NON-EDITABLE --------------------------
    # Khai báo date_added là trường chỉ đọc
    readonly_fields = ('date_added',) 
    
    # Chỉ liệt kê các trường có thể chỉnh sửa trong fields
    fields = ('address', 'city', 'state', 'mobile', 'date_added')
# 3. Custom Admin cho Order (Mục Tổng Hợp Đơn Hàng)
# Sử dụng decorator để tạo mục trên sidebar và liên kết với class OrderAdmin
@admin.register(Order)
class OrderAdmin(admin.ModelAdmin):
    """Mục Tổng hợp Đơn hàng"""
    
    # Các Inline được nhúng vào trang chi tiết Order
    inlines = [OrderItemInline, ShippingAddressInline]
    
    # Các trường hiển thị trong danh sách (list_display)
    list_display = (
        'id', 
        'customer', 
        'date_order', 
        'display_total',  # Hàm hiển thị tổng tiền sau giảm giá
        'display_status', # Hàm hiển thị trạng thái
        'transaction_id',
        'voucher',
    )
    
    # Các trường có thể tìm kiếm
    search_fields = ('id', 'customer__username', 'transaction_id', 'voucher__code')
    
    # Các trường có thể lọc
    list_filter = ('complete', 'date_order')
    
    # Các trường chỉ đọc trong trang chi tiết Order
    readonly_fields = ('date_order', 'discount_amount', 'transaction_id')
    
    # Hàm tùy chỉnh để tính và hiển thị tổng tiền sau khi áp dụng voucher
    def display_total(self, obj):
        total = obj.get_cart_total - obj.discount_amount
        return format_html('<span style="font-weight: bold; color: green;">{} VNĐ</span>', total)
    display_total.short_description = 'Tổng tiền cuối cùng'
    
    # Hàm tùy chỉnh để hiển thị trạng thái bằng màu sắc
    def display_status(self, obj):
        if obj.complete:
            return format_html('<span style="color: green; font-weight: bold;">ĐÃ HOÀN TẤT</span>')
        return format_html('<span style="color: orange; font-weight: bold;">ĐANG XỬ LÝ</span>')
    display_status.short_description = 'Trạng thái'

# 4. Đăng ký các Models còn lại (KHÔNG đăng ký lại Order/OrderItem/ShippingAddress)
admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Payment_VNPay)
admin.site.register(ReviewRating)
admin.site.register(Voucher) 
admin.site.register(ChatMessage)