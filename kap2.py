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

def GenerateMessage(msg,orderMsg,noOfvars,row):
	try:
		orderMsg=orderMsg.split(',')
	except:
		orderMsg=list(orderMsg)
	final_msg=msg
	for i in range(noOfvars):		
		final_msg=final_msg.replace('"VAR{}"'.format(i),row[orderMsg[i]])
	return final_msg


#df is temp dataframe,current is the department,colList is the list of departments
def Send(df,msg,orderMsg,EventName,noOfvars):
	global driver
	for index, row in df.iterrows():
		# try:
		no=str(row['Contact Number'])
		temp_msg=GenerateMessage(msg,orderMsg,int(noOfvars),row)
		# message=msg.format(row[l[0]],row[l[1]])
		print(temp_msg)
			# driver.get(send_message_to_unsavaed_contact('91'+no,msg))
			# wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span'))).click()
			# driver.execute_script("window.onbeforeunload = function() {};")
		# except:
		# 	print(row['Name'])
			



def Load_excel(str_list,msg,orderMsg,noOfvars):
	print(str_list,msg,orderMsg,noOfvars)
	# whatsapp_login()
	try:
		str_list=str_list.split(',')# in case for mutliple values you can pass list
	except:
		str_list=list(str_list)    
	df = pd.read_excel("1.xlsx")
	n=df.shape[0]
	for i in str_list:
		temp_df= df[df[i] == 'Yes']
		Send(temp_df,msg,orderMsg,i,noOfvars)

	



# Load_excel('Hockey','hey "VAR0","VAR1","VAR2" "VAR3"','Name,Department,Present Year,Hockey',4)
