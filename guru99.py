import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.keys import Keys
import time

@pytest.fixture(scope="module")
def setup():
    driver = webdriver.Chrome()
    driver.get("https://demo.guru99.com/test/newtours/register.php")
    yield driver
    driver.quit()

def send_By(driver, by, if_click=0, if_enter=0, **kwargs):
    element = driver.find_element(by, kwargs["param"])
    element.send_keys(kwargs["name"])
    if if_click:
        element.click()
    if if_enter:
        element.send_keys(Keys.ENTER)

def select_by(by, param, value, driver):
    element = driver.find_element(by, param)
    select = Select(element)
    select.select_by_value(value)

def test_registration_form(setup):
    driver = setup

    # Click the registration link
    driver.find_element(By.LINK_TEXT, "REGISTER").click()

    # Fill in the registration form
    send_By(driver, By.NAME, name="Tamar", param="firstName")
    send_By(driver, By.NAME, name="Samara", param="lastName")
    send_By(driver, By.NAME, name="0546837579", param="phone")
    send_By(driver, By.NAME, name="tamar.samara@gmail.com", param="userName")
    send_By(driver, By.NAME, name="Rama", param="address1")
    send_By(driver, By.NAME, name="Rama", param="city")
    send_By(driver, By.NAME, name="-", param="state")
    send_By(driver, By.NAME, name="30055", param="postalCode")

    select_by(param="country", value="ISRAEL", by=By.NAME, driver=driver)

    send_By(driver, By.NAME, name="tamar.samara@gmail.com", param="email")
    send_By(driver, By.NAME, name="12345", param="password")
    send_By(driver, By.NAME, name="12345", param="confirmPassword")

    # Submit the form
    driver.find_element(By.NAME, "submit").click()

    # Wait for the registration to complete
    time.sleep(5)

    # Assert that the registration was successful (you can modify this assertion as needed)
    assert "Thank you for registering" in driver.page_source
