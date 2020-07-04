from selenium import webdriver
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
#Set target name, same as your whatsapp contact
target_name = 'Rana'

def wait(second):
    for i in range(second, 0, -1):
        time.sleep(1)
        yield i

def messageWA():
    print("Scan QR Code")
    print("Waiting to setup whatsapp")
    wait_second = 30
    for countdown in wait(wait_second):
        print(countdown)
    print(f"{wait_second} seconds done")
    try:
        #Search target by its name
        target = driver.find_element_by_xpath(f'//span[@title = "{target_name}"]')
        target.click()
        time.sleep(3)
        try:
            msg_box = driver.find_element_by_class_name('_3uMse')
            #Open and read slumdog-millionaire movie dialogue
            with open('slumdog-millionaire.txt', 'r') as fl:
                texter = fl.read()
                #split dialogue using new line and store in list
                texter = texter.split('\n')
                #iterate each dialogue using loop in msg_box
                for i in range(len(texter)):
                    msg_box.send_keys(f'{texter[i]}')
                    time.sleep(1)
                    button = driver.find_element_by_class_name('_1U1xa')
                    button.click()
        except Exception as err:
            print(err)
    except Exception as err:
        print(err)
    driver.close()

if __name__ == "__main__":
    messageWA()
    print("Done")
