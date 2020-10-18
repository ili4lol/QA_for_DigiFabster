# coding=utf-8

import platform
import pytest

from project.settings import DRIVER_TIMEOUT, USER_EMAIL, USER_PASSWORD, USER_NAME, STREET, CITY, APARTMENT, INDEX, COUNTRY
from project.driver import prepare_driver
os_system = platform.system()

@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    # execute all other hooks to obtain the report object
    outcome = yield
    rep = outcome.get_result()

    # set a report attribute for each phase of a call, which can
    # be "setup", "call", "teardown"

    setattr(item, "rep_" + rep.when, rep)


@pytest.fixture()
def browser():
    driver = prepare_driver()
    driver.timeout = DRIVER_TIMEOUT
    driver.USER_EMAIL = USER_EMAIL
    driver.USER_PASSWORD = USER_PASSWORD
    driver.USER_NAME = USER_NAME
    driver.STREET = STREET
    driver.CITY = CITY
    driver.APARTMENT = APARTMENT
    driver.INDEX = INDEX
    driver.COUNTRY = COUNTRY
    yield driver
    driver.quit()

