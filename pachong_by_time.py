from selenium.webdriver import *
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.common.keys import Keys
#按照月份爬取数据
if __name__ == '__main__':
    web = Firefox()
    web.get("https://huntr.dev/bounties/hacktivity/")
    time.sleep(10)
    last=0
    timedata=web.find_elements(By.XPATH,'//*[@id="hacktivity-table"]/tbody/tr')
    for i in range(len(timedata)):
        if "Apr" in timedata[i].text and ("PHP" in timedata[i].text or "C" in timedata[i].text or "Java" in timedata[i].text or "Python" in timedata[i].text):
            #print(timedata[i].text)
            report=web.find_element(By.XPATH,'/html/body/div[1]/div/div/main/main/div[3]/div/table/tbody/tr['+str(i+1)+']/td/div/div[3]/div[1]/a')
            print(report.get_attribute('href'))
            f = open("e:/test.csv",'a',newline='')
            writer = csv.writer(f)
            writer.writerow([report.get_attribute('href')])
            f.close()
