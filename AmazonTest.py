import unittest
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class amazon(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def test_home(self):

        try:
            driver = self.driver
            driver.get("https://www.amazon.com/")
        except Exception as exception_1:
            print("URL'e ulasilamadi" + exception_1)

        try:
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "nav-link-accountList"))).click()
        except Exception as exception_2:
            print("Login için tiklanamadi" + exception_2)

        try:
            input_ad = driver.find_element_by_id("ap_email")
            input_ad.send_keys("umut.yasin.colak@hotmail.com")
        except Exception as exception_3:
            print("@mail girisi saglanamadi" + exception_3)

        try:
            input_password = driver.find_element_by_id("ap_password")
            input_password.send_keys("Umut0127-")
        except Exception as exception_4:
            print("pasword girisi saglanamadi" + exception_4)

        try:
            login_click_2 = driver.find_element_by_id("signInSubmit")
            login_click_2.click()
        except Exception as exception_5:
            print("Login olunamadi " + exception_5)

        try:
            WebDriverWait(driver, 10).until(ec.presence_of_element_located((By.ID, "twotabsearchtextbox"))).send_keys(
                "samsung", Keys.RETURN)
            assert "samsung" in driver.find_element_by_class_name("a-color-state").text
        except Exception as exception_6:
            print("Arama gerçeklestirilemedi" + exception_6)

        try:
            WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, ".a-normal:nth-child(3)>a"))).click()
            assert "2" in driver.find_element_by_css_selector(".a-selected:nth-child(3)>a").text
        except Exception as exception_7:
            print("2. sayfaya geçilemedi" + exception_7)

        try:
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "div[data-index='0']")))
            product = driver.find_element_by_css_selector("div[data-index='2'] h5 .a-size-medium")
            name = product.text
            product.click()
        except Exception as exception_8:
            print("3. ürün açilamadi" + exception_8)

        try:
            WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((By.ID, "add-to-wishlist-button-submit"))).click()
            time.sleep(1)
        except Exception as exception_9:
            print("ürün listeye eklenemedi" + exception_9)

        try:
            WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, ".a-button-close:nth-child(2)"))).click()
        except Exception as exception_10:
            print("ekleme sayfasi kapatilamadi" + exception_10)

        try:
            element = driver.find_element_by_class_name("nav-truncate")
            ActionChains(driver).move_to_element(element).perform()
            WebDriverWait(driver, 10).until(
                ec.element_to_be_clickable((By.CSS_SELECTOR, ".nav-panel>.nav-link:nth-child(1)>.nav-text"))).click()
        except Exception as exception_11:
            print("menüdeki listeye ulasilamadi" + exception_11)

        try:
            assert name in driver.find_element_by_css_selector("div h3 a").text
        except Exception as exception_12:
            print("listedeki ürün eklenen ürün degil" + exception_12)

        try:
            WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CSS_SELECTOR, "#a-autoid-7"))).click()
            time.sleep(1)
            assert "Deleted" in driver.find_element_by_css_selector(".a-alert-inline-success .a-alert-content").text
        except Exception as exception_13:
            print("Ürünü listeden silemedi" + exception_13)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
