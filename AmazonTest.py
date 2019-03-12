from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.action_chains import ActionChains
import unittest
import time


class amazon(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_home(self):
        driver = self.driver
        driver.get("https://www.amazon.com.tr/")
        time.sleep(2)

        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.ID, "nav-link-accountList"))).click()

        input_ad = driver.find_element_by_id("ap_email")
        input_ad.send_keys("umut.yasin.colak@hotmail.com")
        input_password = driver.find_element_by_id("ap_password")
        input_password.send_keys("Umut0127-")
        login_click_2 = driver.find_element_by_id("signInSubmit")
        login_click_2.click()

        driver.wait_search = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located((By.ID, "twotabsearchtextbox")))
        search = driver.find_element_by_id("twotabsearchtextbox")
        search.send_keys("samsung")
        search.send_keys(Keys.RETURN)
        search_check = driver.find_element_by_xpath("//*[@id='s-result-count']/span/span")
        assert "samsung" in search_check.text

        driver.Wait_click_2page = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='pagn']/span[3]/a")))
        login_click = driver.find_element_by_xpath("//*[@id='pagn']/span[3]/a")
        login_click.click()

        # pg = "2"
        # page2_check = driver.find_element_by_xpath("//*[@id='pagn'']/span[3]")
        # assert pg in page2_check

        driver.Wait_click_product = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='result_17']/div/div/div/div[2]/div[1]/div[1]/a/h2")))
        click_product = driver.find_element_by_xpath("//*[@id='result_17']/div/div/div/div[2]/div[1]/div[1]/a/h2")
        click_product.click()

        driver.Wait_click = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='add-to-wishlist-button-submit']")))
        addlistt = driver.find_element_by_xpath("//*[@id='add-to-wishlist-button-submit']")
        addlistt.click()

        time.sleep(1)
        WebDriverWait(driver, 10).until(ec.element_to_be_clickable((By.CLASS_NAME, "a-button-close"))).click()

        element = driver.find_element_by_class_name("nav-truncate")
        ActionChains(driver).move_to_element(element).perform()

        driver.Wait_click_lists = WebDriverWait(driver, 10).until(
            ec.element_to_be_clickable((By.XPATH, "//*[@id='nav-flyout-wl-items']/div/a/span")))
        click_lists = driver.find_element_by_xpath("//*[@id='nav-flyout-wl-items']/div/a/span")
        click_lists.click()

        time.sleep(6)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
