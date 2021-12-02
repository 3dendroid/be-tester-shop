import time

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

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

# Закрытие окна
driver.quit()
