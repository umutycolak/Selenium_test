import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Locators:
    website_URL = "https://www.amazon.com/"
    login_id = "#nav-link-accountList"
    mail_id = "ap_email"
    mail_text = "umut.yasin.colak@hotmail.com"
    password_id = "ap_password"
    password_text = "Umut0127-"
    login_button = "#signInSubmit"
    input_area = "twotabsearchtextbox"
    search_value = "samsung"
    search_text = ".a-color-state"
    page_button = ".a-selected a"
    page_button2 = ".a-normal a"
    wait_product = "div[data-index='0']"
    product_selector = "div[data-index='2'] h5 .a-size-medium"
    add_list = "#add-to-wishlist-button-submit"
    list_close = ".a-button-close:nth-child(2)"
    move_element = "nav-truncate"
    list_view = ".nav-panel>.nav-link:nth-child(1)>.nav-text"
    list_product = "div h3 a"
    list_product_delete = "#a-autoid-7 .a-button-input"
    delete_check = ".a-alert-inline-success .a-alert-content"
    name = ""
    delete = "Deleted"
    page = "2"
    amazon = "amazon"


class action:

    def click (self, click_Locators):
        WebDriverWait(Driver.driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, click_Locators))).click()

    def Assert (self, value, text_Locators):
        assert value in Driver.driver.find_element_by_css_selector(text_Locators).text

    def url_check(self, amazon, url):
        assert amazon in url

    def get_text (self, Name, text):
        Name == Driver.driver.find_element_by_css_selector(text).text

    def hover (self, hover):
        ActionChains(Driver.driver).move_to_element(Driver.driver.find_element_by_class_name(hover)).perform()

    def input (self, idd, mail):
        Driver.driver.find_element_by_id(idd).send_keys(mail)

    def search(self, input_area, value):
        WebDriverWait(Driver.driver, 10).until(ec.presence_of_element_located((By.ID, input_area))).send_keys(
            value, Keys.RETURN)

class Driver:
    driver = webdriver.Chrome()


class Amazon_test:
    def __init__(self):
        #Stepone
        Driver.driver.get(Locators.website_URL)
        Driver.driver.maximize_window()
        get_class = action()
        get_class.url_check(Locators.amazon, Driver.driver.current_url)
        #Steptwo
        get_class.click(Locators.login_id)
        get_class.input(Locators.mail_id, Locators.mail_text)
        get_class.input(Locators.password_id, Locators.password_text)
        get_class.click(Locators.login_button)
        #StepThree
        get_class.search(Locators.input_area, Locators.search_value)
        #StepFour
        get_class.Assert(Locators.search_value, Locators.search_text)
        #StepFive
        get_class.click(Locators.page_button2)
        get_class.Assert(Locators.page, Locators.page_button)
        #StepSix
        get_class.get_text(Locators.name, Locators.product_selector)
        get_class.click(Locators.product_selector)
        get_class.click(Locators.add_list)
        time.sleep(2)
        get_class.click(Locators.list_close)
        #StepSeven
        get_class.hover(Locators.move_element)
        get_class.click(Locators.list_view)
        #StepEight
        get_class.Assert(Locators.name, Locators.list_product)
        #StepNine
        get_class.click(Locators.list_product_delete)
        #StepTen
        time.sleep(1)
        get_class.Assert(Locators.delete, Locators.delete_check)


Amazon_test()
Driver.driver.close()
