from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
from inputimeout import inputimeout, TimeoutOccurred
from datetime import datetime
from datetime import timedelta
import time


def tp(link, end_time):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("permissions.default.microphone", 1)
    fp.set_preference("permissions.default.camera", 1)
    browser = webdriver.Firefox(firefox_profile=fp)
    browser.get(link)
    name = "BT19MME051 K D S SURYA TEJA"
    email_id = "divijendrasampath4054@gmail.com"
    join = WebDriverWait(browser, float("inf")).until(EC.presence_of_element_located((By.XPATH, '//*[@id="smartJoinButton"]')))
    join.click()
    WebDriverWait(browser, 60).until(EC.frame_to_be_available_and_switch_to_it((By.NAME, "thinIframe")))
    name_field = WebDriverWait(browser, float("inf")).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[2]/div/input")))
    email_field = WebDriverWait(browser, float("inf")).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/div[3]/div[3]/div/input")))
    next_button = WebDriverWait(browser, float("inf")).until(EC.presence_of_element_located((By.XPATH, "//*[@id='guest_next-btn']")))
    name_field.send_keys(name)
    email_field.send_keys(email_id)
    next_button.click()
    time.sleep(3)
    video = WebDriverWait(browser, float("inf")).until(EC.presence_of_element_located((By.CSS_SELECTOR, ".style-has-popup-2x872")))
    mic = WebDriverWait(browser, float("inf")).until(EC.presence_of_element_located((By.CSS_SELECTOR, "div.style-button-container-2_tt5:nth-child(1) > div:nth-child(1) > button:nth-child(1)")))
    video.click()
    mic.click()
    strt = WebDriverWait(browser, float("inf")).until(EC.presence_of_element_located((By.ID, "interstitial_join_btn")))
    time.sleep(3)
    strt.click()
    time_gap = end_time - datetime.now()-timedelta(minutes=10)
    print("Class started")
    time.sleep(time_gap.total_seconds())
    while datetime.now() <= end_time+timedelta(minutes=5):
        try:
            browser.switch_to.default_content()
            WebDriverWait(browser, 60).until(EC.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "#pbui_iframe")))
            ok = WebDriverWait(browser, 60).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div/button")))
            ok.click()
            browser.quit()
            return True
        except TimeoutException:
            if datetime.now()>=end_time+timedelta(minutes=5):
                try:
                    q = inputimeout(prompt='Do you want to quit(y/n)? ', timeout=60)
                except TimeoutOccurred:
                    q="y"
                if q=="y":
                    print("Host did't end the class. But I am quitting the class.")
                    browser.quit()
                    return True
                else:
                    end_time=end_time+timedelta(minutes=5)
                    continue
            else:
                continue

'''
day = datetime.today().day
month = datetime.today().month
yr = datetime.today().year
tp("https://vnit.webex.com/meet/sgsapate",datetime(yr, month, day, 10) )
'''