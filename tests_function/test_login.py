import time
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.implicitly_wait(2)
    yield driver
    driver.close()
    driver.quit()


@pytest.mark.parametrize("email,pw", [
    ('nvhuu.grandm@gmail.com', '12345678'),
    ('nvhuu.grandm@gmail.com', '123456789'),
    ('nvhuu.grandm@gmail.co', '12345678'),
    ('aaaa', '123'),
    ('', '')
])
def test_login_y4(driver, email, pw):
    wrong_pass_mess = "ログインエラー！ パスワードが間違っています。"
    wrong_mess = "ログインエラー！ 入力したメールアドレス、もしくは、パスワードが間違っています。"
    driver.get('https://y4-dev.genkimiru.jp/')
    email_field = driver.find_element(By.CSS_SELECTOR, 'input[name="data[User][email]"].form-control.required')
    pass_field = driver.find_element(By.CSS_SELECTOR, 'input[name="data[User][password]"].form-control.required')
    btn = driver.find_element(By.XPATH, '//button[@class="btn btn-warning btn-lg" and @type="submit"]')

    email_field.send_keys(email)
    pass_field.send_keys(pw)
    btn.click()
    time.sleep(5)
    ex_url = 'https://y4-dev.genkimiru.jp/admin/customers/index'
    alert = driver.find_elements(By.CSS_SELECTOR, 'div.alert.alert-error.alert-dismissible[role="alert"]')
    if alert:
        if alert or wrong_mess in alert[0].text:
            print(" Login failed - The printed message matches the expected message.", alert[0].text)
        elif alert or wrong_pass_mess in alert[0].text:
            print(" Login failed - The printed message matches the expected message.", alert[0].text)
    else:
        assert driver.current_url == ex_url, 'Fail'
        print(" Login successfully")
