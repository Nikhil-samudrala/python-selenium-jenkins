from selenium.webdriver.common.by import By

from utilities.BaseClass import BaseClass


class Login:
    def __init__(self, driver):
        self.driver = driver

    username = (By.NAME, 'username')
    password = (By.NAME, 'password')
    generate_otp_button = (By.XPATH, '//*[@id="app"]/div[2]/div/div[2]/div/div/form/div[2]/button')
    otp_boxes = (By.CLASS_NAME, 'otp-input-text')
    submit_button = (By.CSS_SELECTOR, 'button[type="submit"]')

    def get_login_page(self):
        return self.driver.get(BaseClass.BASE_URL + 'login')

    def get_username(self):
        return self.driver.find_element(*Login.username)

    def get_password(self):
        return self.driver.find_element(*Login.password)

    def get_generate_otp_button(self):
        return self.driver.find_element(*Login.generate_otp_button)

    def get_otp_boxes(self):
        return self.driver.find_elements(*Login.otp_boxes)

    def get_submit_button(self):
        return self.driver.find_element(*Login.submit_button)

