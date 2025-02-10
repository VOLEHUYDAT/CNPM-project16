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

    # Chờ cho hình ảnh có ID 'cart-icon' xuất hiện và nhấn vào nó
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cart-icon"))
    )
    cart_icon.click()
    print("Đã nhấn vào biểu tượng giỏ hàng.")
    time.sleep(10)
except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()