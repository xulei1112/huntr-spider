from selenium.webdriver import *
from selenium.webdriver.common.by import By
import time
import csv
from selenium.webdriver.common.keys import Keys

if __name__ == '__main__':
    web = Firefox()
    web.get("https://huntr.dev/bounties/hacktivity/")
    #
    #for i in range(10):
    #    buttun=web.find_element(By.ID,'pagination')
    #    buttun.click()
    time.sleep(10)
    #try finally提高代码稳定性
    try:
        buttun=web.find_element(By.CSS_SELECTOR,'#hacktivity-page > div.flex.flex-col.sm\:flex-row > div.sm\:ml-4.relative.w-full.sm\:w-1\/2.mt-4.sm\:mt-0 > span > button')
        for i in range(5000):
            buttun.click()
        
    except:
        try:
            buttun2=web.find_element(By.CSS_SELECTOR,'#hacktivity-page > div.flex.flex-col.sm\:flex-row > div.sm\:ml-4.relative.w-full.sm\:w-1\/2.mt-4.sm\:mt-0 > span > button')
            for i in range(5000):
                buttun2.click()
        finally:
            print(2)
    finally:
        print(1)
    element=web.find_elements(By.ID,'report-link')
    sum=0
    for i in element:
        sum+=1
    print(sum)
    f = open("e:/test.csv",'a',newline='')
    #输出最新的漏洞文章的url
    for i in element:
        writer = csv.writer(f)
        writer.writerow([i.get_attribute('href')])
    f.close()
