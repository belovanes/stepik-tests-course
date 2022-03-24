from selenium import webdriver
import math
import pyperclip
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# implicitly_wait(sec) # WebDriver искать каждый элемент в течение 5 секунд
# Explicit Waits (WebDriverWait и expected_conditions)

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/explicit_wait2.html'

try:
    browser.get(url)

    button = browser.find_element_by_css_selector("button#book")

    wait = WebDriverWait(browser, 15)   # driver, timeout, [poll freq in ms]
    wait.until(EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), '$100'))
    button.click()

    x = browser.find_element_by_css_selector("span#input_value").text
    print('x =', x)
    y = str(math.log(abs(12*math.sin(int(x)))))
    print('y =', y)

    inp = browser.find_element_by_xpath("//input[@id='answer']")
    inp.send_keys(y)

    button = browser.find_element_by_css_selector("button#solve")
    print('button found')

   """ ws = browser.window_handles
    print('windows handles before', ws)
    wait = WebDriverWait(browser, 15)  # driver, timeout, poll freq in ms
    # wait.until(EC.new_window_is_opened(ws))
    wait.until(EC.number_of_windows_to_be(4))
    print('windows handles after', browser.window_handles) 
    """

    browser.execute_script("return arguments[0].scrollIntoView(true);", button)
    button.click()

    try:
        alert = browser.switch_to.alert
        st = alert.text
        alert.accept()  # нажатие ОК и закрытие алерта
        print(f'Alert text: {st}')
        pyperclip.copy(st.split(': ')[-1])
        print(f'Clipboard buffer: {pyperclip.paste()}')
    except:
        print('Error in alert switch')
        quit(98)

finally:
    browser.quit()
