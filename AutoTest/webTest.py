from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở trang localhost
    driver.get("http://127.0.0.1:8000/")  # Thay đổi URL nếu cần
    time.sleep(2)  # Đợi 2 giây để trang tải

    # Tìm nút "Add to cart" theo product-id
    product_id = "1"  # Thay đổi ID sản phẩm theo nhu cầu
    add_to_cart_button = driver.find_element(By.XPATH, f"//button[@data-product='{product_id}']")
    
    # Cuộn đến nút
    driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    
    # Đợi một chút để đảm bảo nút đã ở trong tầm nhìn
    time.sleep(3)

    # Nhấn vào nút
    add_to_cart_button.click()
    print("Đã nhấn vào nút 'Add to cart' cho sản phẩm với ID:", product_id)
    product_id = "2"  # Thay đổi ID sản phẩm theo nhu cầu
    add_to_cart_button = driver.find_element(By.XPATH, f"//button[@data-product='{product_id}']")
    
    # Cuộn đến nút
    driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    
    # Đợi một chút để đảm bảo nút đã ở trong tầm nhìn
    time.sleep(3)

    # Nhấn vào nút
    add_to_cart_button.click()
    print("Đã nhấn vào nút 'Add to cart' cho sản phẩm với ID:", product_id)

    product_id = "4"  # Thay đổi ID sản phẩm theo nhu cầu
    add_to_cart_button = driver.find_element(By.XPATH, f"//button[@data-product='{product_id}']")
    
    # Cuộn đến nút
    driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    
    # Đợi một chút để đảm bảo nút đã ở trong tầm nhìn
    time.sleep(3)

    # Nhấn vào nút
    add_to_cart_button.click()
    print("Đã nhấn vào nút 'Add to cart' cho sản phẩm với ID:", product_id)


    

except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    time.sleep(5)
    # Đóng trình duyệt
    driver.quit()

