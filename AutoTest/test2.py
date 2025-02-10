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
    print("Tìm tất cả các liên kết 'View'...")
    view_buttons = WebDriverWait(driver, 10).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "a.btn.btn-outline-success"))
    )
    print(f"Tìm thấy {len(view_buttons)} liên kết 'View'.")

    # Nhấn vào từng liên kết "View"
    for button in view_buttons:
        # Cuộn trang đến nút
        driver.execute_script("arguments[0].scrollIntoView();", button)
        
        # Click vào liên kết
        button.click()
        print("Đã nhấn vào liên kết 'View'.")

        # Đợi một chút để xem kết quả (có thể thay đổi thời gian tùy theo trang)
        time.sleep(5)  # Đợi 5 giây để xem kết quả

        # Quay lại trang trước đó
        driver.back()
        time.sleep(2)  # Đợi 2 giây để trang tải lại

except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()