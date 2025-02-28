import time
import datetime
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

from config import myUser, myPassword, UpdateTime #import variables from config file

if (myUser == "myuser") or (myUser == ""): #Validate username
    print("Invalid Username detected")
    exit()

if (myPassword == "myPassword") or (myPassword == ""): #Validate password
    print("Invalid password detected")
    exit()

if UpdateTime <= 0: #Validate update time
    print("Invalid Update time detected")
    exit()

UpdateTimes = UpdateTime * 3600 #Convert Update time to seconds

while True: #Main loop
    driver = webdriver.Chrome() #initialise chrome as driver
    driver.get("https://ncore.pro/index.php") #load webpage

    field_user = driver.find_element(By.NAME, 'nev') #Locate username text field
    field_pw = driver.find_element(By.NAME, "pass") #Locate password text field
    field_login = driver.find_element(By.CLASS_NAME, 'submit_btn') #Locate login button field

    field_user.send_keys(myUser) #Write username
    field_pw.send_keys(myPassword) #Write password
    field_login.click() #Click on login button

    time.sleep(0.1)

    get_source = driver.page_source #copy the source code
    
    if myUser in get_source: #Check if login was successfull or not. (Search for the username in the source code)
        #Login was successfull
        now = datetime.datetime.now()
        print("succesfully logged in at : ",(now.strftime("%Y-%m-%d %H:%M:%S")))
    else:
        #Login was unsuccessfull
        now = datetime.datetime.now()
        print("login failed at : ",(now.strftime("%Y-%m-%d %H:%M:%S")))

    print("Sleeping for : ", UpdateTime, "H") #print sleeping time

    driver.close(); #closes the current window

    time.sleep(UpdateTimes) #Sleep for the desired time