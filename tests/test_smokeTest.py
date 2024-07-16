# Generated by Selenium IDE
import pytest
import time
import json
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service

class TestSmokeTest():
  def setup_method(self, method):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # Uncomment if you want to run tests in headless mode
    service = Service(r"../chromedriver.exe")
    self.driver = webdriver.Chrome()
    self.vars = {}
  
  def teardown_method(self, method):
    self.driver.quit()
  
  def test_1LogoHeaderandTitle(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".header-logo img")
    assert len(elements) > 0
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h1").text == "Teton Idaho"
    assert self.driver.find_element(By.CSS_SELECTOR, ".header-title > h2").text == "Chamber of Commerce"
    assert self.driver.title == "Teton Idaho CoC"
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > .centered-image")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
    assert len(elements) > 0
    self.driver.close()
  
  def test_2HomePageSpotlightsandJoin(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/index.html")
    self.driver.set_window_size(1233, 1032)
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight1 > p:nth-child(4)")
    assert len(elements) > 0
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".spotlight2 > .centered-image")
    assert len(elements) > 0
    self.driver.find_element(By.LINK_TEXT, "Join Us!").click()
    elements = self.driver.find_elements(By.CSS_SELECTOR, ".join-wizard-main")
    assert len(elements) > 0
    self.driver.close()
  
  def test_3DirectoryGridandListFeature(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/directory.html")
    self.driver.set_window_size(974, 1032)
    self.driver.find_element(By.ID, "directory-grid").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.find_element(By.ID, "directory-list").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".gold-member:nth-child(9) > p:nth-child(2)").text == "Teton Turf and Tree"
    self.driver.close()
  
  def test_4JoinPageDataEntry(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/join.html")
    elements = self.driver.find_elements(By.NAME, "fname")
    assert len(elements) > 0
    self.driver.find_element(By.NAME, "fname").send_keys("Joshua")
    self.driver.find_element(By.NAME, "lname").send_keys("Beale")
    self.driver.find_element(By.NAME, "bizname").click()
    self.driver.find_element(By.NAME, "bizname").send_keys("Stuff n\' Things")
    self.driver.find_element(By.NAME, "biztitle").click()
    self.driver.find_element(By.NAME, "biztitle").send_keys("Jack of All Trades")
    self.driver.find_element(By.NAME, "submit").click()
    elements = self.driver.find_elements(By.NAME, "email")
    assert len(elements) > 0
    self.driver.close()
  
  def test_5AdminPageUsernamePassword(self):
    self.driver.get("http://127.0.0.1:5500/teton/1.6/admin.html")
    elements = self.driver.find_elements(By.ID, "username")
    assert len(elements) > 0
    self.driver.find_element(By.ID, "username").click()
    self.driver.find_element(By.ID, "username").send_keys("user")
    self.driver.find_element(By.ID, "password").click()
    self.driver.find_element(By.ID, "password").send_keys("user")
    self.driver.find_element(By.CSS_SELECTOR, ".mysubmit:nth-child(4)").click()
    assert self.driver.find_element(By.CSS_SELECTOR, ".errorMessage").text == "Invalid username and password."
    self.driver.close()