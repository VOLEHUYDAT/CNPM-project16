from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở trang web
    driver.get("http://127.0.0.1:8000/")  # Thay đổi URL nếu cần

    # Chờ cho hình ảnh có ID 'searched' xuất hiện và nhấn vào nó
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "searched"))
    )
    search.send_keys("Biomilk") 
    time.sleep(1)

    search = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "search"))
    )
    search.click()
    print("Đã nhấn tìm kiếm.")
    time.sleep(1)
    #-----------------------------------------------
    product_id = "1"

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//button[@data-product='{product_id}']"))
    )
    # Cuộn đến nút
    driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    time.sleep(2)
    # Đợi cho nút có thể click được
    add_to_cart_button.click()
    print("Đã nhấn vào nút 'Add to cart' cho sản phẩm với ID:", product_id)
    time.sleep(1.5)
except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()