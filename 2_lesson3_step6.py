from selenium import webdriver
import time
import math
import pyperclip

# Browser Window switching
# new_window = browser.window_handles[1]
# browser.switch_to.window(new_window)
# current_window = browser.current_window_handle


browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/redirect_accept.html'

try:
    browser.get(url)
    button = browser.find_element_by_css_selector("div button.trollface")
    button.click()

    window_list = browser.window_handles
    print(window_list[0].title())
    browser.switch_to.window(browser.window_handles[1])

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
