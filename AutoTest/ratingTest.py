from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import random
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở trang web
    driver.get("http://127.0.0.1:8000/")  # Thay đổi URL nếu cần
    time.sleep(3)
    
    login = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "login"))
    )
    login.click()
    print("Đã nhấn vào login.")
    time.sleep(1)
    # Điền dữ liệu vào trường "username"
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("admin") 
    time.sleep(1)
    # Điền dữ liệu vào trường "password"
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("admin")
    time.sleep(1)  
    # Nhấn nút "Login"
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("Đã nhấn nút 'Login'.")
    time.sleep(2)

    product_id = "12"
    
    view_button = WebDriverWait(driver, 10).until(
       EC.presence_of_element_located((By.XPATH, f"//a[contains(@href, '?id={product_id}') and contains(text(), 'View')]"))
    )

    # Cuộn đến nút
    driver.execute_script("arguments[0].scrollIntoView();", view_button)
    time.sleep(2)
    # Đợi cho nút có thể click được
    view_button.click()
    print("Đã nhấn vào nút 'View' cho sản phẩm với ID:", product_id)
    time.sleep(1.5)



    # Chọn số sao ngẫu nhiên (từ 0.5 đến 5)
    rating_value = random.choice(["3", "3.5", "4", "4.5", "5"])

    # Xác định ID của ngôi sao cần click
    rating_id = f"rating{int(float(rating_value) * 2)}"

    # Click vào `<label>` thay vì `<input>`
    rating_label = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, f"//label[@for='{rating_id}']"))
    )

    # Cuộn vào tầm nhìn rồi click
    # Cuộn vào tầm nhìn
    driver.execute_script("arguments[0].scrollIntoView();", rating_label)
    time.sleep(1)

    # Click bằng JavaScript (tránh bị CSS chặn)
    driver.execute_script("arguments[0].click();", rating_label)
    print(f"Đã chọn {rating_value} sao bằng label (JS).")

    # Click thêm vào input nếu cần
    driver.execute_script("document.getElementById(arguments[0]).click();", rating_id)
    print(f"Đã chọn {rating_value} sao bằng input (JS).")
    time.sleep(2)


    subject_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "subject"))
    )
    subject_input.send_keys("Mua sữa sỉ") 
    time.sleep(1)

    review_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "review"))
    )
    review_input.send_keys("sữa ngon bổ rẻ chất lượng cao.") 
    time.sleep(1)
    # Đợi cho phần tử xuất hiện và có thể click được
    submit_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div/div/div/div/div[2]/div/div[3]/div/form/div/input[2]"))
    )

    # Cuộn vào tầm nhìn rồi click
    driver.execute_script("arguments[0].scrollIntoView();", submit_button)
    time.sleep(1)

    # Click vào nút
    submit_button.click()
    print("Đã bấm vào nút submit.")

except Exception as e:
    print("Đã xảy ra lỗi:", e)
    time.sleep(10)
finally:
    # Đóng trình duyệt
    time.sleep(3)
    driver.quit()