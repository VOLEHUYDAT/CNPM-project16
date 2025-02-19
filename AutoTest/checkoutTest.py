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
    driver.get("http://127.0.0.1:8000/checkout/")  # Thay đổi URL nếu cần
    time.sleep(2)


    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name_input.send_keys("Huydat") 
    time.sleep(1)

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys("huydat13825@gmail.com") 
    time.sleep(1)

    address_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "address"))
    )
    address_input.send_keys("Phường 25, Bình Thạnh") 
    time.sleep(1)

    city_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "city"))
    )
    city_input.send_keys("Hồ Chí Minh") 
    time.sleep(1)

    state_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "state"))
    )
    state_input.send_keys("TP. Hồ Chí Minh") 
    time.sleep(1)

    phone_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "mobile"))
    )
    phone_input.send_keys("0987654321") 
    time.sleep(1)
    
    country_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "country"))
    )
    country_input.send_keys("Việt Nam") 
    time.sleep(1)
    
    # Nhấn nút "Payment"
    payment_button = driver.find_element(By.NAME, "payment-button")
    ActionChains(driver).move_to_element(payment_button).perform()

    # Nhấn vào nút
    payment_button.click()
    print("Đã nhấn nút 'Payment'.")
    time.sleep(5)
except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()