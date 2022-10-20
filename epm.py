from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from datetime import datetime
from datetime import timedelta
import time


def epm(link, end_time):
    fp = webdriver.FirefoxProfile()
    fp.set_preference("permissions.default.microphone", 1)
    fp.set_preference("permissions.default.camera", 1)
    browser = webdriver.Firefox(firefox_profile=fp)
    browser.get(link)
    time.sleep(30)
    name = "BT19MME051 KONIKI DIVIJENDRA SAMPATH SURYA TEJA"
    email_id = "divijendrasampath4054@gmail.com"
    while datetime.now() <= end_time:
        try:
            WebDriverWait(browser, 10).until(
                EC.frame_to_be_available_and_switch_to_it((By.NAME, "mainFrame")))
            browser.switch_to.frame(1)
            user_name = browser.find_element_by_id("join.label.userName")
            email_field = browser.find_element_by_id("join.label.emailAddress")
            join = browser.find_element_by_id("ec-btn-joinnow-thin-client")
            user_name.send_keys(name)
            email_field.send_keys(email_id)
            join.click()
            browser.switch_to.default_content()
            WebDriverWait(browser, 60).until(
                EC.frame_to_be_available_and_switch_to_it((By.NAME, "mainFrame")))
            WebDriverWait(browser, 60).until(
                EC.frame_to_be_available_and_switch_to_it((By.NAME, "main")))
            time.sleep(10)
            browser.switch_to.frame(0)
            action = ActionChains(browser)
            computer_audio = WebDriverWait(browser, 60).until(
                EC.presence_of_element_located((By.ID, "conn-voip")))
            connect = WebDriverWait(browser, 60).until(EC.presence_of_element_located(
                (By.XPATH, "/html/body/div[3]/div/div/div[2]/div/div[2]/div/div/div[2]/div[1]/span[3]/button")))
            action.move_to_element(computer_audio).click(connect).perform()
            print("Class started.")
            time_gap = end_time - datetime.now()-timedelta(minutes=15)
            time.sleep(time_gap.total_seconds())
            while datetime.now() <= end_time+timedelta(minutes=15):
                try:
                    ok = WebDriverWait(browser, 600).until(EC.presence_of_element_located(
                        (By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div/button")))
                    ok.click()
                    browser.quit()
                    return True
                except TimeoutException:
                    continue
        except:
            print("Class has not yet started. I will try again in 60 sec.")
            time.sleep(60)
            browser.refresh()
            continue
        print("Class might have been cancelled.")
        return False
