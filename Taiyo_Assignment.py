
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup
import requests
import pandas as pd

driver = webdriver.Chrome('D:/Web Scraping/chromedriver_win32/chromedriver.exe')
driver.get('https:www.google.com')


google_input = driver.find_element(By.XPATH,'/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input')
google_input.send_keys('https://etenders.gov.in/eprocure/app')
google_input.send_keys(Keys.ENTER)

gov_input = driver.find_element(By.XPATH,'//*[@id="rso"]/div[1]/div/div/div/div/div/div/div[1]/a/div/cite').click()


tenders_closing = driver.find_element(By.XPATH,'//*[@id="For_1"]')
tenders_closing.click()

tender_closing_within_14_days = driver.find_element(By.XPATH,'//*[@id="LinkSubmit_1"]/span').click()


soup = BeautifulSoup(driver.page_source,'lxml')


tender_table = soup.find('table',class_='list_table')

headers = ['S.No','e-Published Date','Bid Submission Closing Date','Tender Opening Date','Title and Ref.No/Tender ID','Organisation Chain']
internal_values = []
for data in tender_table.find_all('tbody'):
    rows = data.find_all('tr')
    for i in range(1,len(rows)):
        internal_values.append(rows[i].text.replace("\t",'').strip())



new_internal_values = [s.replace('\n','') for s in internal_values]
print(new_internal_values)


tender_data = pd.DataFrame(columns=headers)

tender_data.to_csv('D:/Tender.csv')








          
    









