from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.parse
import xlrd 


driver = None
Link = "https://web.whatsapp.com/"
wait = None

def whatsapp_login():
    global wait, driver, Link
    # options=Options()
    # options.addArguments("--disable-popup-blocking");
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")

def send_message_to_unsavaed_contact(number,msg):
    # Reference : https://faq.whatsapp.com/en/android/26000030/
    # print("In send_message_to_unsavaed_contact method")
    params = {'phone': str(number), 'text': str(msg)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    # print(final_url)
    return final_url
    



def excel_load():
    global driver
    # Give the location of the file 
    loc = ("1.xlsx") 
    # To open Workbook 
    wb = xlrd.open_workbook(loc) 
    sheet = wb.sheet_by_index(0) 
    print(sheet.nrows)
    for i in range(1,sheet.nrows):
        try:
            no=str(int(sheet.cell_value(i, 1)))
            msg='Hey {}. '.format(sheet.cell_value(i, 0).capitalize())
            driver.get(send_message_to_unsavaed_contact('91'+no,msg))
            wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span'))).click()
            driver.execute_script("window.onbeforeunload = function() {};")
        except:
            print(i+1)


whatsapp_login()
excel_load()
