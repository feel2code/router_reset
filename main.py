'''rebooting router via http, cause it is not have telnet or ssh'''

import time
# import os
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import socket
opts = Options()
# driver_path = os.path.dirname(os.path.abspath(__file__))


def reset(ip_address: str):
    # driver = webdriver.Firefox(executable_path = driver_path + '/machine',
    # service_log_path = None , options = opts)
    driver = webdriver.Firefox('C:/geckodriver.exe', service_log_path=None,
                               options=opts)
    driver.get(ip_address)

    def click(xpath):
        status = False
        while not status:
            try:
                driver.find_element_by_xpath(xpath).click()
                status = True
            except:
                time.sleep(1)

    click('/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]/div'
          '/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]')
    status = False
    while not status:
        try:
            driver.find_element_by_xpath(
              '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]'
              '/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]'
              '/input[1]').send_keys('cekka2-dyzViq-vuhgyf')
            status = True
        except:
            time.sleep(1)
    status = False
    while not status:
        try:
            driver.find_element_by_xpath(
                '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]'
                '/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]'
                '/input[1]').send_keys(Keys.ENTER)
            status = True
        except:
            time.sleep(1)
    time.sleep(4)
    status = False
    while not status:
        try:
            driver.get(ip_address + '#reboot')
            status = True
        except:
            time.sleep(1)
    time.sleep(4)
    click('/html/body/div[1]/div/div[1]/div/div[2]/div[2]/div/div[2]/div[1]'
          '/div[3]/div[1]/div[2]/div[2]/div[2]/div/div/div[2]/div[1]/a')
    time.sleep(2)
    click('/html/body/div[5]/div[7]/div[4]/div/div/div[2]/div/div[2]/div'
          '/div[2]/div[1]/a/span[2]')
    time.sleep(5)
    driver.quit()
    print('ok')


# checking internet
def connection():
    try:
        # host = socket.gethostbyname('http://www.ya.ru')
        host = socket.gethostbyname('ya.ru')
        s = socket.create_connection((host, 80), 5)
        s.close()
        return True
    except:
        return False


# if internet is not working - rebooting the router
while True:
    time.sleep(5)
    if connection() is True:
        print('ok')
        time.sleep(5)
    else:
        print('internet is down. rebooting...')
        try:
            reset('http://192.168.0.100')
        except:
            try:
                reset('http://192.168.0.101')
            except:
                try:
                    reset('http://192.168.0.102')
                except:
                    try:
                        reset('http://192.168.0.103')
                    except:
                        print('something gone wrong. call to administrator.')
                        time.sleep(200)
        time.sleep(100)
    time.sleep(5)
