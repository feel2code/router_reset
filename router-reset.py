import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.firefox.options import Options
import socket

# import os
# driver_path = os.path.dirname(os.path.abspath(__file__))

opts = Options()
main = 'http://192.168.0.'


def reset(ip_address: str):
    '''reset router'''
    # driver = webdriver.Firefox(executable_path = driver_path + '/selenium-gecko',
    # service_log_path = None , options = opts)
    driver = webdriver.Firefox('C:/geckodriver.exe', service_log_path=None,
                               options=opts)
    driver.get(ip_address)

    def click(xpath):
        '''click on element by xpath'''
        status = False
        while not status:
            try:
                driver.find_element_by_xpath(xpath).click()
                status = True
            except:
                time.sleep(1)

    def send_key(xpath, act):
        '''send keys by xpath'''
        status = False
        while not status:
            try:
                driver.find_element_by_xpath(xpath).send_keys(act)
                status = True
            except:
                time.sleep(1)

    click(
        '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]/div'
        '/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]/input[1]')
    send_key(
        '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]'
        '/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]'
        '/input[1]', 'cekka2-dyzViq-vuhgyf')
    send_key(
        '/html/body/div[1]/div/div[1]/div/div[1]/div[2]/div[3]/div[3]'
        '/div/div/div[2]/div[2]/div[2]/div[1]/div[2]/div[1]/span[2]'
        '/input[1]', Keys.ENTER)
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


def connection():
    '''checking internet'''
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
        for last_address in range(100, 116):
            print('internet is down. rebooting...')
            try:
                reset(main + last_address)
            except:
                print(
                    'something gone wrong. trying next IP address:',
                    main + last_address
                )
        time.sleep(100)
