from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep

# def test_sale():
#     session = webdriver.Chrome()
#     session.get('https://magento.softwaretestingboard.com/')
#     sleep(10)
#     sale_link = session.find_element(By.ID, 'ui-id-8')
#     sale_link.click()
#     title = session.find_element(By.TAG_NAME, 'h1')
#     assert title.text == 'Sale'

def test_pMaster():
    session = webdriver.Chrome()
    session.get('https://prazdnikmaster.ru/catalog/geliy_i_oborudovanie/geliy/gaz_geliy_obem_40_l_5_24_m3/')
    sleep(2)
    assert "6200" == "".join((session.find_element(By.CLASS_NAME, 'price_value').text).split())
