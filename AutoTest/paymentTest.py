from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở trang localhost
    driver.get("http://127.0.0.1:8000/payment")  # Thay đổi URL nếu cần
    time.sleep(2)  # Đợi 2 giây để trang tải

    # Chọn ngân hàng NCB
    bank_code_select = driver.find_element(By.ID, 'bank_code')
    bank_code_select.click()
    ncb_option = driver.find_element(By.XPATH, "//option[@value='NCB']")
    ncb_option.click()
    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()

    time.sleep(5)
except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()