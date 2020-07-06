import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Config:
    current_url = "https://www.amazon.com/"
    search_text = ""
    product_name = ""
    deleted_value_to_check = "Deleted"
    page_check = "2"
    referans_url = "https://www.amazon.com/"
    page_value = ""

class Locators:
    main_page_login_button = "#nav-link-accountList"
    mail_input = "ap_email"
    password_input = "ap_password"
    login_page_button = "#signInSubmit"
    search_input = "twotabsearchtextbox"
    search_text_check = ".a-color-state"
    selected_page_button = ".a-selected a"
    unselected_page_button = ".a-normal a"
    product = "div[data-index='"+Config.page_value+"'] h5 .a-size-medium"
    add_list = "#add-to-wishlist-button-submit"
    list_close = ".a-button-close:nth-child(2)"
    move_list = "nav-truncate"
    list_view = ".nav-panel>.nav-link:nth-child(1)>.nav-text"
    list_product = ".a-size-base a"
    list_product_delete = "#a-autoid-7 .a-button-input"
    delete_check = ".a-alert-inline-success .a-alert-content"


class Action:
    def __init__(self):
        self.driver = Drivers.Chrome

    def click(self, click_element):
        click_css = (By.CSS_SELECTOR, click_element)
        wait = WebDriverWait(self.driver, 10).until(ec.element_to_be_clickable(click_css))
        wait.click()

    def Assert(self, check_value, value_to_check):
        assert check_value in self.driver.find_element_by_css_selector(value_to_check).text

    def url_check(self, current_url, referans_url):
        assert current_url == referans_url

    def hoverList(self):
        hover_element_class = self.driver.find_element_by_class_name(Locators.move_list)
        hover = ActionChains(self.driver).move_to_element(hover_element_class)
        hover.perform()

    def input(self, selector, value):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, selector))).send_keys(
            value)

    def search(self, input_area, value):
        WebDriverWait(self.driver, 10).until(ec.presence_of_element_located((By.ID, input_area))).send_keys(
            value, Keys.RETURN)


class Drivers:
    Chrome = webdriver.Chrome()


class HomePage:
    def __init__(self):
        self.get_class = Action()

    def loginButtonclick(self):
        return self.get_class.click(Locators.main_page_login_button)

    def searchinput(self, search_text):
        Config.search_text = search_text
        self.get_class.search(Locators.search_input, Config.search_text)

    def list_view_click(self):
        self.get_class.click(Locators.list_view)


class LoginPage:
    def __init__(self):
        self.get_class = Action()

    def login(self, mail_text, password_text):

        self.get_class.input(Locators.mail_input, mail_text)
        self.get_class.input(Locators.password_input, password_text)
        self.get_class.click(Locators.login_page_button)


class SearchPage:
    def __init__(self):
        self.get_class = Action()
        self.driver = Drivers.Chrome

    def different_page_click(self):
        self.get_class.click(Locators.unselected_page_button)

    def click_3_product(self):
        self.get_class.click(Locators.product)

    def get_product_name(self, value):
        Config.page_value = value
        Locators.product = "div[data-index='" + Config.page_value + "'] h5 .a-size-medium"
        Config.product_name == self.driver.find_element_by_css_selector(Locators.product).text


class ProductPage:
    def __init__(self):
        self.get_class = Action()

    def addlist(self):
        self.get_class.click(Locators.add_list)
        time.sleep(2)

    def closelist(self):
        self.get_class.click(Locators.list_close)


class ListPage:
    def __init__(self):
        self.get_class = Action()

    def delete(self):
        self.get_class.click(Locators.list_product_delete)
        time.sleep(1)


class Amazon_test:
    def __init__(self):
        # wakeup
        self.driver = Drivers.Chrome
        self.Action = Action()
        self.HomePage = HomePage()
        self.LoginPage = LoginPage()
        self.SearchPage = SearchPage()
        self.ProductPage = ProductPage()
        self.ListPage = ListPage()
        self.driver.get(Config.current_url)
        self.driver.maximize_window()


        # Stepone
        self.Action.url_check(Config.referans_url, Config.current_url)
        # Steptwo
        self.HomePage.loginButtonclick()
        self.LoginPage.login("***********@hotmail.com", "*******")
        # StepThree
        self.HomePage.searchinput("samsung")
        # StepFour
        self.Action.Assert(Config.search_text, Locators.search_text_check)
        # StepFive
        self.SearchPage.different_page_click()
        self. Action.Assert(Config.page_check, Locators.selected_page_button)
        # StepSix
        self.SearchPage.get_product_name("6")
        self.SearchPage. click_3_product()
        self.ProductPage.addlist()
        self.ProductPage.closelist()
        # StepSeven
        self.Action.hoverList()
        self.HomePage.list_view_click()
        # StepEight
        self.Action.Assert(Config.product_name, Locators.list_product)
        # StepNine
        self.ListPage.delete()
        # StepTen
        time.sleep(1)
        self.Action.Assert(Config.deleted_value_to_check, Locators.delete_check)


Amazon_test()
Drivers.Chrome.quit()
