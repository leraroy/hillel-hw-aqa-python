"""
Выбрать общедоступный веб-ресурс.
Написать 5 XPath и 5 CSS локаторов для элементов страницы.
Это могут быть одни и те же элементы или разные.
Добавить скриншот с обведенными элементами, для которых вы пишете локаторы.
Для каждого элемента использовать разные подходы в написании локаторов
(т.е. не должно быть что все 5 локаторов записаны по id).
"""
from selenium import webdriver
from selenium.webdriver.common.by import By

# XPath
catalog_xpath = "//button[@id='fat-menu']"
computers_notebooks_xpath = "//div[@class='fat-wrap']//a[contains(@href, 'computers')]"
open_menu_xpath = "(//header//button)[1]"
search_xpath = "//input[@name='search']"
submit_button_xpath = "//form/button[contains(@class,'submit')]"
# CSS
catalog_css = "#fat-menu"
computers_notebooks_css = ".fat-wrap a[href*='computers']"
open_menu_css = ".header-menu button:first-child"
search_css = "[name='search']"
submit_button_css = "form [class*='submit']"

driver = webdriver.Firefox()
driver.maximize_window()
driver.implicitly_wait(5)
driver.get("https://rozetka.com.ua/ua/")

catalog_xpath_element = driver.find_element(By.XPATH, catalog_xpath)
print(catalog_xpath_element.is_displayed())
catalog_css_element = driver.find_element(By.CSS_SELECTOR, catalog_css)
print(catalog_xpath_element.is_displayed())

computers_notebooks_xpath_element = driver.find_element(By.XPATH, computers_notebooks_xpath)
print(computers_notebooks_xpath_element.is_displayed())
computers_notebooks_css_element = driver.find_element(By.CSS_SELECTOR, computers_notebooks_css)
print(computers_notebooks_css_element.is_displayed())

open_menu_xpath_element = driver.find_element(By.XPATH, open_menu_xpath)
print(open_menu_xpath_element.is_displayed())
open_menu_css_element = driver.find_element(By.CSS_SELECTOR, open_menu_css)
print(open_menu_css_element.is_displayed())

search_xpath_element = driver.find_element(By.XPATH, search_xpath)
print(search_xpath_element.is_displayed())
search_css_element = driver.find_element(By.CSS_SELECTOR, search_css)
print(search_css_element.is_displayed())

submit_button_xpath_element = driver.find_element(By.XPATH, submit_button_xpath)
print(submit_button_xpath_element.is_displayed())
submit_button_css_element = driver.find_element(By.CSS_SELECTOR, submit_button_css)
print(submit_button_css_element.is_displayed())

driver.quit()
