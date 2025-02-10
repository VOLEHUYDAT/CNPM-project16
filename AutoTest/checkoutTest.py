from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
import time
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở trang web
    driver.get("http://127.0.0.1:8000/")  # Thay đổi URL nếu cần
    time.sleep(2)

    register = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "register"))
    )
    register.click()
    print("Đã nhấn vào register.")
    time.sleep(1)

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("Huydat3") 
    time.sleep(1)

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys("huydat13825@gmail.com") 
    time.sleep(1)

    first_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "first_name"))
    )
    first_name_input.send_keys("Dat") 
    time.sleep(1)

    last_name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "last_name"))
    )
    last_name_input.send_keys("Huy") 
    time.sleep(1)

    password1_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password1"))
    )
    password1_input.send_keys("volehuydat1") 
    time.sleep(1)

    password2_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "password2"))
    )
    password2_input.send_keys("volehuydat1") 
    time.sleep(1)
    # Nhấn nút "register"
    register_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    register_button.click()
    print("Đã nhấn nút 'Register'.")
    time.sleep(2)
except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()