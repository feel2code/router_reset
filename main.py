import time
import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import socket
opts = Options()
driver_path = os.path.dirname(os.path.abspath(__file__))

def reset():
    driver = webdriver.Firefox(executable_path = driver_path + '/machine', service_log_path = None , options = opts)
    driver.get('http://192.168.0.100')
    status = False
    while not status:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]').click()
            status = True
        except:
            time.sleep(1)
    status = False
    while not status:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]').send_keys('cekka2-dyzViq-vuhgyf')
            status = True
        except:
            time.sleep(1)
    status = False
    while not status:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]').send_keys(Keys.ENTER)
            status = True
        except:
            time.sleep(1)
    time.sleep(4)
    status = False
    while not status:
        try:
            driver.get('http://192.168.0.100/#reboot')
            status = True
        except:
            time.sleep(1)
    time.sleep(4)
    status = False
    while not status:
        try:
            driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/a').click()
            status = True
        except:
            time.sleep(1)
    time.sleep(2)
    status = False
    while not status:
        try:
            driver.find_element_by_xpath('/html/body/div[5]/div[7]/div[4]/div/div/div[2]/div/div[2]/div/div[2]/div[1]/a/span[2]').click()
            status = True
        except:
            time.sleep(1)
    time.sleep(5)
    driver.quit()
    print('ok')

def connection():
    try:
        host = socket.gethostbyname('http://www.ya.ru')
        s = socket.create_connection((host, 80), 5)
        s.close()
        return True
    except:
        return False


while True:
    time.sleep(5)
    if connection() == True:
        print('ok')
        time.sleep(5)
    else:
        print('internet is down. rebooting...')
        reset()
    time.sleep(5)
