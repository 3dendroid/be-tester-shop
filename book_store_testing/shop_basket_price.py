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

# Нажатие на вкладку My Account Menu
my_account = driver.find_element(By.LINK_TEXT, 'My Account')
my_account.click()

# Ввод почты
time.sleep(2)
email = driver.find_element(By.ID, 'username')
email.send_keys('somemail@gmail.com')

# Ввод  пароля
time.sleep(2)
password = driver.find_element(By.ID, 'password')
password.send_keys('Py_bB2%worD)')

# Нажатие на кнопку Login
time.sleep(2)
register_btn = driver.find_element(By.CSS_SELECTOR, '[name="login"]')
register_btn.click()

# Нажатие на раздел Shop
shop = driver.find_element(By.LINK_TEXT, 'Shop')
shop.click()
time.sleep(2)

# Добавление книги HTML5 WebApp Development в корзину
book_2_basket = driver.find_element(By.CSS_SELECTOR, '[href="/shop/?add-to-cart=182"]')
book_2_basket.click()
time.sleep(2)

# Проверка количества товаров и стоимости в корзине
basket_count = driver.find_element(By.CSS_SELECTOR, '[class="cartcontents"]').text
print(basket_count)
assert basket_count == '1 Item'

basket_cost = driver.find_element(By.CSS_SELECTOR, '[class="amount"]').text
print(basket_cost)
assert basket_cost == '₹180.00'

# Проход в корзину
basket = driver.find_element(By.XPATH, '//*[@id="wpmenucartli"]/a')
basket.click()

# Проверка стоимости в Subtotal
subtotal = wait.until(
    EC.text_to_be_present_in_element((By.XPATH, '//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[1]/td/span'),
                                     text_='₹180.00'))

# Проверка стоимости в Total
total = wait.until(EC.text_to_be_present_in_element((By.XPATH,
                                                     '//*[@id="page-34"]/div/div[1]/div/div/table/tbody/tr[3]/td/strong/span'),
                                                    text_='₹189.00'))

# Закрытие окна
driver.quit()
