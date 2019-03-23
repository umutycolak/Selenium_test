import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Locators:
    website_URL = "https://www.amazon.com/"
    login_id = "nav-link-accountList"
    mail_id = "ap_email"
    mail_text = "umut.yasin.colak@hotmail.com"
    password_id = "ap_password"
    password_text = "Umut0127-"
    login_button = "signInSubmit"
    input_area = "twotabsearchtextbox"
    search_value = "samsung"
    search_text = "a-color-state"
    page_button = ".a-selected a"
    wait_product = "div[data-index='0']"
    product_selector = "div[data-index='2'] h5 .a-size-medium"
    add_list = "add-to-wishlist-button-submit"
    list_close = ".a-button-close:nth-child(2)"
    move_element = "nav-truncate"
    list_view = ".nav-panel>.nav-link:nth-child(1)>.nav-text"
    list_product = "div h3 a"
    list_product_delete = "#a-autoid-7 .a-button-input"
    delete_check = ".a-alert-inline-success .a-alert-content"
    name = ""
    delete = "Deleted"


class Driver:
    driver = webdriver.Chrome()


class Amazon_test:
    class StepOne:

        def __init__(self):
            Driver.driver.get(Locators.website_URL)
            assert "amazon" in Driver.driver.current_url

    class StepTwo:

        def __init__(self):
            WebDriverWait(Driver.driver, 10).until(ec.element_to_be_clickable((By.ID, Locators.login_id))).click()
            input_ad = Driver.driver.find_element_by_id(Locators.mail_id)
            input_ad.send_keys(Locators.mail_text)
            input_password = Driver.driver.find_element_by_id(Locators.password_id)
            input_password.send_keys(Locators.password_text)
            login_click_2 = Driver.driver.find_element_by_id(Locators.login_button)
            login_click_2.click()

    class StepThree:
        def __init__(self):
            WebDriverWait(Driver.driver, 10).until(
                ec.presence_of_element_located((By.ID, Locators.input_area))).send_keys(
                Locators.search_value, Keys.RETURN)

    class StepFour:
        def __init__(self):
            assert Locators.search_value in Driver.driver.find_element_by_class_name(Locators.search_text).text

    class StepFive:
        def __init__(self):
            WebDriverWait(Driver.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, Locators.page_button))).click()
            assert "2" in Driver.driver.find_element_by_css_selector(Locators.wait_product).text

    class StepSix:
        def __init__(self):
            WebDriverWait(Driver.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, Locators.wait_product)))
            product = Driver.driver.find_element_by_css_selector(Locators.product_selector)
            Locators.name = product.text
            product.click()
            WebDriverWait(Driver.driver, 10).until(
                ec.element_to_be_clickable((By.ID, Locators.add_list))).click()
            time.sleep(2)
            WebDriverWait(Driver.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, Locators.list_close))).click()

    class StepSeven:
        def __init__(self):
            element = Driver.driver.find_element_by_class_name(Locators.move_element)
            ActionChains(Driver.driver).move_to_element(element).perform()
            WebDriverWait(Driver.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, Locators.list_view))).click()

    class StepEight:
        def __init__(self):
            assert Locators.name in Driver.driver.find_element_by_css_selector(Locators.list_product).text

    class StepNine:
        def __init__(self):
            WebDriverWait(
                Driver.driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, Locators.list_product_delete))).click()

    class StepTen:
        def __init__(self):
            time.sleep(1)
            assert Locators.delete in Driver.driver.find_element_by_css_selector(Locators.delete_check).text

    class start:
        def __init__(self):
            Locators()
            Amazon_test.StepOne()
            Amazon_test.StepTwo()
            Amazon_test.StepThree()
            Amazon_test.StepFour()
            Amazon_test.StepFive()
            Amazon_test.StepSix()
            Amazon_test.StepSeven()
            Amazon_test.StepEight()
            Amazon_test.StepNine()
            Amazon_test.StepTen()
            Driver.driver.close()


Amazon_test.start()
