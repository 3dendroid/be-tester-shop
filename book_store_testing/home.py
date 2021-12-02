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

# Скролл страницы на 600 единиц
driver.execute_script("window.scrollBy(0, 600);")

# Выбор книги Selenium Ruby
book = driver.find_element(By.CSS_SELECTOR, 'a > h3')
book.click()

# Нажатие на вкладку Reviews
reviews = driver.find_element(By.CSS_SELECTOR, '[class="reviews_tab"]')
reviews.click()

# Поставить 5 звёзд
five_star = driver.find_element(By.LINK_TEXT, '5')
five_star.click()

# Заполнение поля отзыва
review = driver.find_element(By.ID, 'comment')
review.send_keys('Nice book!')

# Заполнение поля Name
name = driver.find_element(By.ID, 'author')
name.send_keys('John')

# Заполнение поля Email
name = driver.find_element(By.ID, 'email')
name.send_keys('JohnSmith@gmail.com')

# Нажатие на кнопку Submit
submit_btn = driver.find_element(By.ID, 'submit')
submit_btn.click()

# Закрытие окна
driver.quit()
