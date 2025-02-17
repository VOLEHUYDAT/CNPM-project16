from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Khởi tạo trình duyệt Chrome
driver = webdriver.Chrome()

try:
    # Mở trang có dropdown menu
    driver.get('http://127.0.0.1:8000/')  # Thay đổi URL nếu cần

    # Chờ cho trang tải xong
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.ID, 'category')))

    # Nhấn vào dropdown để mở menu
    dropdown = driver.find_element(By.ID, 'category')
    dropdown.click()
    time.sleep(2)
    # Chờ cho các mục con xuất hiện
    WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'dropdown-item')))

    # Lấy tất cả các mục con trong dropdown
    sub_items = driver.find_elements(By.CLASS_NAME, 'dropdown-item')

    # Nhấn vào từng mục con
    for item in sub_items:
        item_name = item.text  # Lấy tên mục con
        print(f"Nhấn vào mục: {item_name}")
        item.click()  # Nhấn vào mục con

        # Chờ một chút để xem kết quả (có thể cần điều chỉnh)
        time.sleep(1)

        # Quay lại trang trước đó để nhấn vào mục con tiếp theo
        driver.back()

        # Chờ cho dropdown menu mở lại
        dropdown.click()
        WebDriverWait(driver, 10).until(EC.presence_of_all_elements_located((By.CLASS_NAME, 'dropdown-item')))
        time.sleep(1)
    advertise = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "advertise"))
    )
    advertise.click()
    time.sleep(2)

    contact = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "contact"))
    )
    contact.click()
    time.sleep(2)

    message_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "message"))
    )
    message_input.send_keys("Hello") 
    time.sleep(1)

    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name_input.send_keys("Huy Dat") 
    time.sleep(1)

    email_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "email"))
    )
    email_input.send_keys("huydat13825@gmail.com") 
    time.sleep(1)

    send_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    send_button.click()
    print("Đã nhấn nút 'Send'.")
    time.sleep(2)
    #------------------------------------------------------
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
    time.sleep(3)

    back = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "back"))
    )
    back.click()
    print("Đã nhấn vào back.")
    time.sleep(3)
    #-------------------------------------------------------------------------
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