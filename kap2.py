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
missed=[]
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
	for i in range(1,noOfvars+1):		
		final_msg=final_msg.replace('"VAR{}"'.format(i),str(row[orderMsg[i-1]]))
	return final_msg


#df is temp dataframe,current is the department,colList is the list of departments
def Send(df,msg,orderMsg,EventName,noOfvars):
	global driver,missed
	for index, row in df.iterrows():
		try:
			no=str(row['Contact Number'])
			temp_msg=''
			temp_msg=GenerateMessage(msg,orderMsg,int(noOfvars),row)
			if(temp_msg==''):
				missed.append(row['Name'])
				continue
			print(temp_msg)
			driver.get(send_message_to_unsavaed_contact('91'+no,temp_msg))
			wait.until(EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span'))).click()
			driver.execute_script("window.onbeforeunload = function() {};")
		except:
			missed.append(row['Name'])
	if(len(missed)>0):
		print(missed)
			



def Load_excel(str_list,msg,orderMsg,noOfvars):
	global missed
	missed=[]
	if(noOfvars==''):
		noOfvars=0
	# print(str_list,msg,orderMsg,noOfvars)
	whatsapp_login()
	str_list=str(str_list)    
	df = pd.read_excel("1.xlsx")
	try:
		temp_df= df[df[str_list] == 'Yes']
	except:
		temp_df=df
	Send(temp_df,msg,orderMsg,str_list,noOfvars)

	



# Load_excel('Hockey','hey "VAR1","VAR2" "VAR3"','Name,Department,Present Year',3)
