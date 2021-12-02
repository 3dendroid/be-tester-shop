import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait

# Параметры для запуска ведбрайвера
path_to_extension = r'C:\Users\denki\AppData\Local\Google\Chrome\User Data\Default\Extensions\gighmmpiobklfepjocnamgkkbiglidom\4.40.0_0'
chrome_options = Options()
chrome_options.add_argument('load-extension=' + path_to_extension)
driver = webdriver.Chrome(r'C:\Users\denki\Desktop\BE-tester\automation\chromedriver\chromedriver.exe',
                          options=chrome_options)
driver.create_options()
time.sleep(10)
driver.maximize_window()
driver.implicitly_wait(5)
url = 'http://practice.automationtesting.in/'
wait = WebDriverWait(driver, 10)

# Установка расширения Adblock и закрытие окна, открытие нового окна
driver.close()
time.sleep(1)
first_tab = driver.window_handles[0]
driver.switch_to.window(first_tab)
driver.get(url)
time.sleep(2)

# Нажатие на раздел Shop
shop = driver.find_element(By.LINK_TEXT, 'Shop')
shop.click()
time.sleep(2)

# Скролл на 300 пикселей вниз, добавление книги HTML5 WebApp Development в корзину
driver.execute_script("window.scrollBy(0, 300);")
book_2_basket_1 = driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=182"]')
book_2_basket_1.click()
time.sleep(2)

# Добавление книги JS Data Structures and Algorithm в корзину
book_2_basket_2 = driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=180"]')
book_2_basket_2.click()
time.sleep(2)

# Проход в корзину
basket = driver.find_element(By.XPATH, '//*[@id="wpmenucartli"]/a')
basket.click()

# Удаление первой книги из корзины
time.sleep(2)
remove = driver.find_element(By.CSS_SELECTOR, '[class="remove"]')
remove.click()

# Нажатие на Undo
undo = driver.find_element(By.LINK_TEXT, 'Undo?')
undo.click()

# Увеличение количества для второй книги
quantity = driver.find_element(By.CSS_SELECTOR, '.cart_item:nth-child(2)>td:nth-child(5)>div>input')
value = quantity.get_attribute('value')
quantity.clear()
quantity.send_keys(3)

# Нажатие на кнопку Update Basket
update_btn = driver.find_element(By.CSS_SELECTOR, '[name="update_cart"]')
update_btn.click()
time.sleep(2)

# Проверка value=3 для JS Data Structures and Algorithm
quantity = driver.find_element(By.CSS_SELECTOR, '.cart_item:nth-child(2)>td:nth-child(5)>div>input')
quantity_text = quantity.get_attribute('value')
assert quantity_text == '3'

# Нажатие на кнопку Apply Coupon
time.sleep(3)
apply_btn = driver.find_element(By.CSS_SELECTOR, '.coupon>input:nth-child(3)')
apply_btn.click()
time.sleep(3)

# Проверка сообщения
# text = "Please enter a coupon code."
time.sleep(3)
text = driver.find_element(By.CSS_SELECTOR, '.woocommerce-error>li').text
assert text == 'Please enter a coupon code.'

# Закрытие окна
driver.quit()
