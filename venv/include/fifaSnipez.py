from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.keys import Keys
import time

caps = DesiredCapabilities().CHROME
caps["pageLoadStrategy"] = "none"

options = webdriver.ChromeOptions()
options.add_argument('--user-data-dir=C:/Users/Administrator/AppData/Local/Google/Chrome/User Data/Profile1')
options.add_argument('--profile-directory=Profile1')
browser = webdriver.Chrome(executable_path='/Users/finn/Downloads/chromedriver', options=options, desired_capabilities=caps)
browser.get("https://www.easports.com/fifa/ultimate-team/web-app/")


xpath_manipulation_field = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[5]/div[2]/input"
xpath_min_bid_price = "/html/body/main/section/section/div[2]/div/div[2]/div/div[1]/div[2]/div[2]/div[2]/input"
css_selector_players_body = "body > main > section > section > div.ut-navigation-container-view--content > div > div > section.ut-navigation-container-view.ui-layout-right > div > div > div.DetailPanel > div.bidOptions > button.btn-standard.buyButton.currency-coins"
xpath_transfer_market = "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[1]/button/span[1]"
xpath_min_sell_price = "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[2]/div[2]/input"
xpath_max_sell_price = "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/div[3]/div[2]/input"
xpath_list_on_market = "/html/body/main/section/section/div[2]/div/div/section[2]/div/div/div[2]/div[2]/div[2]/button"

time.sleep(15)
x = 1
y = 10250
second_param = 0
while x == 1:
    try:
        browser.find_element_by_xpath("/html/body/div[4]/section/div/p")
        print("Error")
    except:
        pass
    resellBid = 20000
    resellBuy = 27750
    try:
        y += 250
        if y >= 15000:
            if second_param == 0:
                y = 10250
            else:
                y = second_param
            '''if second_param == 0:
                second_param = 150
                browser.find_element_by_xpath(xpath_min_bid_price).clear()
                browser.find_element_by_xpath(xpath_min_bid_price).send_keys(second_param)
                y = second_param + 50
            elif second_param == 150:
                second_param = 200
                browser.find_element_by_xpath(xpath_min_bid_price).clear()
                browser.find_element_by_xpath(xpath_min_bid_price).send_keys(second_param)
                y = second_param + 50
            elif second_param == 200:
                second_param = 250
                browser.find_element_by_xpath(xpath_min_bid_price).clear()
                browser.find_element_by_xpath(xpath_min_bid_price).send_keys(second_param)
                y = second_param + 50
            else:
                second_param = 0
                browser.find_element_by_xpath(xpath_min_bid_price).clear()
                browser.find_element_by_xpath(xpath_min_bid_price).send_keys(second_param)'''
        eraser = browser.find_element_by_xpath(xpath_manipulation_field)
        eraser.clear()
        time.sleep(0.2)
        eraser.send_keys(str(y))
        time.sleep(0.2)
        searchPlayer = browser.find_element_by_xpath(
            "/html/body/main/section/section/div[2]/div/div[2]/div/div[2]/button[2]")
        searchPlayer.click()
        time.sleep(0.5)
        counter_until_go_back = 0
        while counter_until_go_back <= 35:
            time.sleep(0.01)
            if len(browser.find_elements_by_css_selector(css_selector_players_body)) > 0:
                browser.find_element_by_css_selector(css_selector_players_body).click()
                wait1 = WebDriverWait(browser, 4)
                waitPurchase = wait1.until(ec.visibility_of_element_located((By.XPATH, "/html/body/div[4]/section/div/div/button[1]")))
                waitPurchase.click()
                time.sleep(1.5)
                try:
                    transferMarket = browser.find_element_by_xpath(xpath_transfer_market).click()
                    time.sleep(1)
                    bidMin = browser.find_element_by_xpath(xpath_min_sell_price)
                    bidMin.click()
                    time.sleep(3)
                    bidMin.send_keys(Keys.BACKSPACE, resellBid)
                    time.sleep(3)
                    sellMin = browser.find_element_by_xpath(xpath_max_sell_price)
                    sellMin.click()
                    time.sleep(3)
                    sellMin.send_keys(Keys.BACKSPACE, resellBuy)
                    time.sleep(3)
                    list_on_market = browser.find_element_by_xpath(xpath_list_on_market)
                    list_on_market.click()
                    time.sleep(2)
                except:
                    counter_until_go_back = 50
                    pass
                time.sleep(2)
            else:
                counter_until_go_back += 1

        goBack = browser.find_element_by_xpath("/html/body/main/section/section/div[1]/button[1]")
        goBack.click()
        WebDriverWait(browser, 4).until(ec.element_to_be_clickable((By.XPATH, xpath_min_bid_price)))
        time.sleep(0.25)
    except:
        continue