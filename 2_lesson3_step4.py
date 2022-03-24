from selenium import webdriver
import time
import math
import pyperclip

# confirm, alert and promt

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/alert_accept.html'

try:
    browser.get(url)

    button = browser.find_element_by_xpath("//div/button")
    button.click()

    try:
        alert = browser.switch_to.alert
        alert.accept()  # нажатие ОК и закрытие алерта
        # alert.dismiss() # нажатие Cancel и закрытие алерта
        # alert.send_keys() #ввод данных в строку алерта (prompt)
    except:
        print('Error in alert switch')
        quit(99)

    x = browser.find_element_by_id("input_value").text
    print('x =', x)
    y = str(math.log(abs(12*math.sin(int(x)))))
    print('y =', y)

    inp = browser.find_element_by_xpath("//input[@id='answer']")
    inp.send_keys(y)

    button = browser.find_element_by_css_selector("button.btn")
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
    time.sleep(2)
    browser.quit()
