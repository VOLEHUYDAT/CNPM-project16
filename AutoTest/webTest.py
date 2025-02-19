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
    time.sleep(3)
    
    register = WebDriverWait(driver, 10).until(
    EC.element_to_be_clickable((By.ID, "register"))
    )
    register.click()
    print("Đã nhấn vào register.")
    time.sleep(1)

    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )
    username_input.send_keys("Huydat642") 
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
    #---------------------------------------------------------------
    # Điền dữ liệu vào trường "username"
    username_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    username_input.send_keys("Huydat642") 
    time.sleep(1)
    # Điền dữ liệu vào trường "password"
    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("volehuydat1")
    time.sleep(1)  
    # Nhấn nút "Login"
    login_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    login_button.click()
    print("Đã nhấn nút 'Login'.")
    time.sleep(2)
    #--------------------------------------------------
    # Danh sách các product ID cần thêm vào giỏ hàng
    product_id = "4"

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
    #--------------------------------------------------
    product_id = "4"

    add_to_cart_button = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, f"//button[@data-product='{product_id}']"))
    )
    # Cuộn đến nút
    driver.execute_script("arguments[0].scrollIntoView();", add_to_cart_button)
    
    time.sleep(2)

    add_to_cart_button.click()
    print("Đã nhấn vào nút 'Add to cart' cho sản phẩm với ID:", product_id)
    time.sleep(2)
    #--------------------------------------------------

    # Chờ cho hình ảnh có ID 'searched' xuất hiện và nhấn vào nó
    search = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "searched"))
    )
    search.send_keys("Biomil") 
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

    #--------------------------------------------------
    cart_icon = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "cart-icon"))
    )
    cart_icon.click()
    print("Đã nhấn vào biểu tượng giỏ hàng.")
    time.sleep(1)

    checkout = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "checkout"))
    )
    checkout.click()
    print("Đã nhấn Checkout.")
    time.sleep(3)

    #----------------------------------------------------------------------
    name_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "name"))
    )
    name_input.send_keys("Huy Đạt") 
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
    #------------------------------------------------------------------
    bank_code_select = driver.find_element(By.ID, 'bank_code')
    bank_code_select.click()
    ncb_option = driver.find_element(By.XPATH, "//option[@value='NCB']")
    ncb_option.click()
    time.sleep(2)
    submit_button = driver.find_element(By.XPATH, "//button[@type='submit']")
    submit_button.click()
    #--------------------------------------------------------------
    cardNumber_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "card_number_mask"))
    )
    cardNumber_input.send_keys("9704198526191432198") 
    time.sleep(1)
    
    cardHolder_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cardHolder"))
    )
    cardHolder_input.send_keys("Nguyen Van A") 
    time.sleep(1)

    cardDate_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "cardDate"))
    )
    cardDate_input.send_keys("07/15") 
    time.sleep(1)

    btnContinue = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnContinue")) 
    )
    btnContinue.click()
    time.sleep(2)

    btnAgreeContinue = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Đồng ý & Tiếp tục']"))  # Sử dụng XPath để tìm phần tử
    )

    # Nhấp vào nút "Đồng ý & Tiếp tục"
    btnAgreeContinue.click()

    # Tùy chọn: Chờ một giây để quan sát (không khuyến khích trong mã sản xuất)
    time.sleep(2)

    otpvalue_input = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "otpvalue"))
    )
    otpvalue_input.send_keys("123456") 
    time.sleep(1)

    btnConfirm = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "btnConfirm")) 
    )
    btnConfirm.click()
    time.sleep(3)

    backHome = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "backHome")) 
    )
    backHome.click()
    time.sleep(2)
    time.sleep(5)
except Exception as e:
    print("Đã xảy ra lỗi:", e)

finally:
    # Đóng trình duyệt
    driver.quit()