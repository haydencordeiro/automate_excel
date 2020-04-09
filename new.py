from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from time import sleep
import urllib.parse
import pandas as pd 

driver = None
Link = "https://web.whatsapp.com/"
wait = None

def whatsapp_login():
    global wait, driver, Link
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 20)
    print("SCAN YOUR QR CODE FOR WHATSAPP WEB IF DISPLAYED")
    driver.get(Link)
    driver.maximize_window()
    print("QR CODE SCANNED")

def send_message_to_unsavaed_contact(number,msg):
    # Reference : https://faq.whatsapp.com/en/android/26000030/
    params = {'phone': str(number), 'text': str(msg)}
    end = urllib.parse.urlencode(params)
    final_url = Link + 'send?' + end
    return final_url



def Send(df,current):
	global driver
	for index, row in df.iterrows():
		try:
			no=str(row['Contact Number'])
			msg=message[colList.index(current)].format(row['Full Name'])
			driver.get(send_message_to_unsavaed_contact('91'+no,msg))
			wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span'))).click()
			driver.execute_script("window.onbeforeunload = function() {};")
		except:
			# driver.find_element_by_xpath('//*[@id="app"]/div/span[2]/div/span/div/div/div/div/div/div[2]/div').click()
			print(row['Full Name'])
			



def Load_excel(str_list):    
	df = pd.read_excel("1.xlsx")
	n=df.shape[0]
	for i in str_list:
		temp_df= df[df[i] != 'No']
		Send(temp_df,i)

	

whatsapp_login()
colList=['Football','Hockey']
message=['Hey {} thanks for participating in footbal',
'Hey {} thanks for participating in Hocket'
]
Load_excel(colList)