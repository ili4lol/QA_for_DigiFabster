# coding=utf-8
import allure
from allure.constants import AttachmentType
import os
import time


@allure.feature('Тесты Digifabster')
@allure.story('Клиенский заказ')
def test_client_order(browser):
    """
    Наименование сценария:
    Клиенский заказ


    Шаг 1. Открытие страницы

    """

    with allure.step('Шаг 1. Открытие страницы'):
        try:
            browser.open()
            allure.attach('screenshot', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
        except:
            allure.attach('error_screen', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 2. Регистрация'):
        try:
            browser.registration(browser.USER_EMAIL, browser.USER_NAME, browser.USER_PASSWORD)
            allure.attach('screenshot', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
        except:
            allure.attach('error_screen', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 3. Загрузка файла'):
        try:
            xpath = ".//*[@id='import-drop-target']/p[1]/a/input"
            file = os.path.abspath('project/tests/files/test.stl ')
            browser.download_file(xpath, file)
            browser.wait_xpath(".//*[@id='import-drop-target']/div[3]/div/div/div[4]/div[1]")
            time.sleep(5)
            browser.xpath('//div[@class="pull-right"]').click()
            allure.attach('screenshot', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
        except:
            allure.attach('error_screen', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 4. Переход в корзину'):
        try:
            time.sleep(15)
            browser.xpath('//*[@id="s2"]/div[2]/div/div[2]/div[1]/div[3]').click()
            time.sleep(15)
            browser.xpath('/html/body/div[3]/div/div[2]/div/div[5]/div[3]/div').click()
            time.sleep(15)
            browser.xpath('//*[@id="invalid_m_type_cost_msg"]/strong[2]/p/span[2]').click()
            browser.xpath('/html/body/div[3]/div/div[2]/div/div[2]/div[3]/a').click()
            allure.attach('screenshot', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
        except:
            allure.attach('error_screen', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise

    with allure.step('Шаг 5. Доставка'):
        try:
            browser.xpath('//*[@id="main_form"]/div[2]/div[1]/input').send_keys("89999999999")
            browser.xpath('//*[@id="main_form"]/div[1]/div[2]/input').send_keys("test")
            browser.add_order_address(browser.STREET, browser.CITY, browser.APARTMENT, browser.INDEX, browser.COUNTRY)
            browser.xpath('//*[@id="delivery_address_wrapper"]/div[1]/div[1]/input').send_keys("test")
            time.sleep(10)
            browser.xpath('//*[@id="s4_submit"]').click()
            time.sleep(10)
            browser.xpath('//*[@id="s4_submit"]').click()
            browser.xpath('//*[@id="place_order_form"]/button').click()
            browser.xpath('//*[@id="system_message"]')
            allure.attach('screenshot', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
        except:
            allure.attach('error_screen', browser.get_screenshot_as_png(), type=AttachmentType.PNG)
            raise