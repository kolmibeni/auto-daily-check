from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from time import sleep
import time
import os
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import sys  
reload(sys)  
sys.setdefaultencoding('utf8')
driver = webdriver.Chrome()

def wait_for_ajax(driver):
    wait = WebDriverWait(driver, 15)
    try:
        wait.until(lambda driver: driver.execute_script('return jQuery.active') == 0)
        wait.until(lambda driver: driver.execute_script('return document.readyState') == 'complete')
    except Exception as e:
        pass
        driver.quit()
        fp.close();
driver.get('https://app.pers.ncku.edu.tw/ncov/index.php?c=fp&bid=D201&rid=D20105017&floor=5F')

# LOGIN
search_input = driver.find_element_by_css_selector(
       '#user_id')
search_input.send_keys('10710070')
search_input = driver.find_element_by_css_selector(
       '#passwd')
search_input.send_keys('Auto63906#')
order_tab = driver.find_element_by_css_selector(
       'button[class=\"btn btn-default\"]')
order_tab.click()
sleep(5)

# CLOSE DIALOG
order_tab = driver.find_element_by_css_selector(
       'button[class=\"btn btn-primary\"]')
order_tab.click()
sleep(5)

# FILL INFO
order_tab = driver.find_element_by_css_selector(
       '#fs_upd_N')
order_tab.click()
sleep(5)
order_tab = driver.find_element_by_css_selector(
       'button[class=\"btn btn-primary save_button\"]')
order_tab.click()
sleep(5)


#for record in checkinList:
#   fp.write('record:'+record.text) 

# RECORD LOG
# date-of-record=driver.find_element_by_css_selector(
#     'div[class=\"green-bg\"]')
# date-of-record=driver.find_element_by_css_selector(
#     'div[class=\"green-bg\"]')
#user=driver.find_element_by_css_selector(
#    'button[class=\"btn btn-success pull-left\"]')
# wait_for_ajax(driver)
# print(user.get_attribute('innerHTML'))
print("Daily check-up successful")

fp = open("C:\\log.txt", "a")
localtime = time.asctime( time.localtime(time.time()))
# fp.write(localtime+':'+user.get_attribute('innerHTML')+'\n')
fp.write(localtime+': SUCCESS')

# CLOSE DIALOG
order_tab = driver.find_element_by_css_selector(
       'button[class=\"btn btn-primary\"]')
order_tab.click()
sleep(5)

driver.quit()
fp.close();
