import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
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
book_2_basket_1 = driver.find_element(By.CSS_SELECTOR, '.post-182>a:nth-child(2)')
book_2_basket_1.click()
time.sleep(2)

# Проход в корзину
basket = driver.find_element(By.XPATH, '//*[@id="wpmenucartli"]/a')
basket.click()

# Нажатие на кнопку Proceed to checkout
time.sleep(2)
proceed = driver.find_element(By.CSS_SELECTOR, 'div:nth-child(3)>a')
proceed.click()

# Заполнение полей Checkout
# Ввод имени
first_name = driver.find_element(By.CSS_SELECTOR, '[name="billing_first_name"]')
first_name.send_keys('Severus')
time.sleep(2)

# Ввод фамилии
last_name = driver.find_element(By.CSS_SELECTOR, '[name="billing_last_name"]')
last_name.send_keys('Snape')
time.sleep(2)

# Ввод почты
email = driver.find_element(By.CSS_SELECTOR, '[name="billing_email"]')
email.send_keys('severusape@hogwarts.com')
time.sleep(2)

# Ввод телефона
phone = driver.find_element(By.CSS_SELECTOR, '[name="billing_phone"]')
phone.send_keys('+29718576348')
time.sleep(2)

# Выбор страны
country = driver.find_element(By.CSS_SELECTOR, 'p>div')
country.click()
time.sleep(2)
write_country = driver.find_element(By.ID, 's2id_autogen1_search')
write_country.send_keys('Afghanistan')
time.sleep(2)
select_afghanistan = driver.find_element(By.CSS_SELECTOR, '[class="select2-match"]')
time.sleep(2)
select_afghanistan.click()

# Ввод адреса
address = driver.find_element(By.CSS_SELECTOR, '[name="billing_address_1"]')
address.send_keys('Diagon Alley, 33')
time.sleep(2)

# Ввод города
city = driver.find_element(By.CSS_SELECTOR, '[name="billing_city"]')
city.send_keys('Warsaw')
time.sleep(2)

# Ввод кода страны
postcode = driver.find_element(By.CSS_SELECTOR, '[name="billing_postcode"]')
postcode.send_keys('46580')
time.sleep(2)

# Скролл вниз на 600 пикселей, и выбор радиокнопки Check Payments
driver.execute_script("window.scrollBy(0, 600);")
check_payment = driver.find_element(By.ID, 'payment_method_cheque')
check_payment.click()
time.sleep(3)

# Нажатие на кнопку Place order
place_order = driver.find_element(By.CSS_SELECTOR, '[id="place_order"]')
place_order.click()

# Проверка надписи с явным ожиданием
text = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div>div>p:nth-child(1)'),
                                                   'Thank you. Your order has been received.'))

# Проверка Payment Method с явным ожиданием
payment_method = wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, 'div>ul>li:nth-child(4)'),
                                                             'Check Payments'))

# Закрытие окна
driver.quit()
