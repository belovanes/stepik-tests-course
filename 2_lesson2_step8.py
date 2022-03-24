from selenium import webdriver
import time
import math
import os
import pyperclip



# upload file, path for file

browser = webdriver.Chrome()
url = 'http://suninjuly.github.io/file_input.html'
fname = 'file.txt'
fdir = os.path.abspath(os.path.dirname(__file__))
print('fname=', fname)
print('fdir=', fdir)

try:
    browser.get(url)
    # elements = browser.find_elements_by_css_selector("input[type='text']")
    # x = browser.find_element_by_xpath("//label/span[@id='input_value']").text

    inp1 = browser.find_element_by_name("firstname")
    inp1.send_keys('Женя')

    inp2 = browser.find_element_by_name("lastname")
    inp2.send_keys('Жопа')

    inp3 = browser.find_element_by_name("email")
    inp3.send_keys('Шума')

    finp = browser.find_element_by_xpath("//input[@type='file']")
    finp.send_keys(fdir+'\\'+fname)

    button = browser.find_element_by_xpath("//button[@type='submit']")
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

finally:
    time.sleep(1)
    browser.quit()
