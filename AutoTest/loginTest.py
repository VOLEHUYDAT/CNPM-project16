HEAD
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time

# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở trang localhost
    driver.get("http://127.0.0.1:8000/")  # Thay đổi URL nếu cần
    time.sleep(2)  # Đợi 2 giây để trang tải
    
    login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login"))
    )
    login.click()
    print("Đã nhấn vào login.")
    time.sleep(1)

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("thuongg") 
    time.sleep(1)
    # Điền dữ liệu vào trường "password"
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("Thuong2209@a")
    time.sleep(1)  
    # Nhấn nút "Login"
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("Đã nhấn nút 'Login'.")
    time.sleep(2)
    

except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    time.sleep(5)
    # Đóng trình duyệt
    driver.quit()

