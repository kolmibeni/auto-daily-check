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
driver.get('https://eadm.ncku.edu.tw/welldoc/ncku/iftwd/signIn.php')
search_input = driver.find_element_by_css_selector(
       '#psnCode')
search_input.send_keys('10710070')
search_input = driver.find_element_by_css_selector(
       '#password')
search_input.send_keys('Auto63906#')
order_tab = driver.find_element_by_css_selector(
       'button[class=\"btn btn-small pull-left\"]')
order_tab.click()
sleep(1)

#for record in checkinList:
#   fp.write('record:'+record.text) 


user=driver.find_element_by_css_selector(
    'span[data-ng-bind=\"listTitle\"]')
#user=driver.find_element_by_css_selector(
#    'button[class=\"btn btn-success pull-left\"]')
wait_for_ajax(driver)
print(user.get_attribute('innerHTML'))

fp = open("C:\\log.txt", "a")
localtime = time.asctime( time.localtime(time.time()))
fp.write(localtime+':'+user.get_attribute('innerHTML')+'\n')

checkinList = driver.find_elements_by_css_selector('#checkinList td')
record=''
i=1
for item in checkinList:
    record = record+ '('+item.get_attribute('innerHTML')+') '
    if(i%5==0):
        print(record)
        fp.write(record+'\n')
        record=''
    i=i+1

driver.quit()
fp.close();
