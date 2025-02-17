from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở trang localhost
    driver.get("http://127.0.0.1:8000/")  # Thay đổi URL nếu cần
    time.sleep(2)  # Đợi 2 giây để trang tải

    # Tìm tất cả các liên kết "View"
   

except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()