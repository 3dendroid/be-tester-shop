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

# Открытие книги Android Quick Start Guide
book = driver.find_element(By.CSS_SELECTOR, '[alt="Android Quick Start Guide"]')
book.click()

# Проверка старой цены
old_price = driver.find_element(By.CSS_SELECTOR, 'p.price > del > span').text
old_price_digits = ''.join([n for n in old_price if n.isdigit()])[0:3]
print(old_price_digits)
assert old_price_digits == '600'

# Проверка новой цены
new_price = driver.find_element(By.CSS_SELECTOR, 'p.price > ins > span').text
new_price_digits = ''.join([n for n in new_price if n.isdigit()])[0:3]
print(new_price_digits)
assert new_price_digits == '450'

# Нажатие на обложку книги с явным ожиданием

book_img = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="images"]')))
book_img.click()

# Закрытие окна просмотра книги с явным ожиданием
close = wait.until(EC.element_to_be_clickable((By.CSS_SELECTOR, '[class="pp_close"]')))
close.click()

# Закрытие окна
driver.quit()
