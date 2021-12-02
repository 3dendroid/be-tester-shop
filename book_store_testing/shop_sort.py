import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

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

# Проверка селектора сортировки
sort = driver.find_element(By.NAME, 'orderby')
sort_value = Select(sort).select_by_value('menu_order')
sort_selected = sort.get_attribute('selected')
if sort_value == sort_selected:
    print('Выбрана сортировка по умолчанию')
else:
    print('Выбрана другая сортировка')

# Сортировка товара от большого к меньшему
sort_from_high_2_low = Select(sort).select_by_value('price-desc')

# Повторная проверка селектора сортировки
sort = driver.find_element(By.NAME, 'orderby')
sort_selected = sort.get_attribute('selected')
if sort_from_high_2_low == sort_selected:
    print('Выбрана сортировка от большего к меньшему')
else:
    print('Выбрана другая сортировка')

# Закрытие окна
driver.quit()
