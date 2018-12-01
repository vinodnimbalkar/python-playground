from selenium import webdriver
import pandas as pd
import time

driver = webdriver.Chrome()
driver.get('https://web.whatsapp.com/')
print("Scan QR Code")
print("Waiting to setup whatsapp")
time.sleep(50)

def messageWA():
    #Create Your contact list csv and save as "contact_list.csv"
    df = pd.read_csv("contact_list.csv")
    print("50 seconds done")
    for i in range(len(df)):
        name = df.iloc[i,0]
        try:
            #Message to send peoples
            msg = "May this Diwali your life be as colourful and bright as the lights of Diwali. Joy and gaiety surround you and your family forever. Happy Diwali!"
            #Number of time send above message
            count = 1

            #Open new chat section screen
            new_chat = driver.find_element_by_xpath('//*[@id="side"]/header/div[2]/div/span/div[2]/div')
            new_chat.click()
            time.sleep(3)

            #Search contact list people available on whatsapp or not
            search_box = driver.find_element_by_class_name('jN-F5')
            search_box.send_keys(str(name))
            time.sleep(3)
            try:
                #Open message box of user by name in contact list
                user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(str(name)))
                user.click()
                time.sleep(3)
            except:
                #if User not available on whatsapp, back to initial screen
                backButton = driver.find_element_by_class_name('_1aTxu')
                backButton.click()
                time.sleep(3)
                continue
            try:
                msg_box = driver.find_element_by_class_name('_2S1VP')

                #Loop for number of type above message send
                for i in range(count):
                    msg_box.send_keys(msg)
                    button = driver.find_element_by_class_name('_35EW6')
                    button.click()
                    #Create log text file of successfully sent message with user name
                    with open("successSend.txt", "a") as successLog:
                        successLog.write("Successfully send :"+str(name)+"\n")
                    print("Successfully send :"+str(name))
                    break
            except:
                #Create log file of failed message with user name
                with open("contactLog.txt","a") as errLog:
                    errLog.write(str(name)+"\n")
                print("msg failed to :"+str(name)+" "+str(err))   
            
        except Exception as err:
                print("Error in New Chat or Search Box"+str(err))

if __name__ == "__main__":
    messageWA()
    print("Done")