# coding=utf-8

""" Основной Page Object от которого инициализируются все остальные Page Object классы
"""


import time
from seleniumwrapper import SeleniumWrapper
from selenium.common.exceptions import WebDriverException


class Page(SeleniumWrapper):
    def open(self):
        """ Открывает страницу
        """
        self.delete_all_cookies()
        self.get("https://digifabster.com/4taps/client/upload/")
        self.xpath(".//*[@id='import-drop-target']/p[1]/a/input")

    def registration(self, email, name, password):
        """ Регистрация
        """
        self.xpath("/html/body/div[3]/div/div[1]/div[2]/div/a").click()
        self.xpath("/html/body/div[3]/div/div[1]/div[2]/div/ul/li[2]/a").click()
        self.xpath("/html/body/div[3]/div/div[3]/form/div[1]/input").send_keys(email)
        self.xpath("/html/body/div[3]/div/div[3]/form/div[2]/input").send_keys(name)
        self.xpath("/html/body/div[3]/div/div[3]/form/div[3]/input").send_keys(password)
        self.xpath("/html/body/div[3]/div/div[3]/form/div[4]/input").send_keys(password)
        self.xpath("/html/body/div[3]/div/div[3]/form/div[5]/button").click()

    def auth(self, email, password):
        """
        Авторизация
        """
        self.xpath('//*[@id="id_get_user_email_form-email"]').send_keys(email)
        self.xpath('//*[@id="set_email"]/span').click()
        time.sleep(2)
        self.xpath('//*[@id="id_password"]').send_keys(password)
        time.sleep(2)
        self.xpath('//*[@id="auth_btn"]').click()
        time.sleep(2)

    def add_order_address(self, street, city, apartment, index, country):
        self.xpath('//*[@id="delivery_address_wrapper"]/div[1]/div[2]/input').send_keys(street)
        self.xpath('//*[@id="delivery_address_wrapper"]/div[2]/div[2]/input').send_keys(city)
        self.xpath('//*[@id="delivery_address_wrapper"]/div[2]/div[1]/input').send_keys(apartment)
        self.xpath('//*[@id="delivery_address_wrapper"]/div[3]/div[1]/input').send_keys(index)
        self.xpath('//*[@id="delivery_address_wrapper"]/div[3]/div[2]/div/input').send_keys(country)
        self.xpath('//*[@id="delivery_address_wrapper"]/div[3]/div[2]/div/ul/li[108]').click()

    def download_file(self, xpath, file):
        """ Загружает файл
        """
        self.scroll_to_element(xpath)
        self.xpath(xpath).send_keys(file)

    def is_xpath_present(self, xpath, eager=False, timeout=1, presleep=0):
        """ Проверяет существую ли указанный элемент
        """
        time.sleep(presleep)
        self.silent = True
        elements = self.xpath(xpath, eager=eager, timeout=timeout)
        self.silent = False
        if eager:
            return elements

        if not elements:
            return []

        if elements.is_displayed():
            return True

    def wait_xpath(self, xpath, timeout=None, raise_errors=False):
        """ Дожидается появления элемента в течении n сек
        """
        timeout = timeout or self.timeout
        for _ in range(timeout):
            if self.is_xpath_present(xpath):
                return True
            time.sleep(1)
        if raise_errors:
            raise WebDriverException(f'{xpath} is not visible')


class NotFound(Exception):
    pass
