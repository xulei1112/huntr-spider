from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import csv

if __name__ == '__main__':
    web = Chrome()
    web.get("https://huntr.dev/bounties/hacktivity/")
    #
    #for i in range(10):
    #    buttun=web.find_element(By.ID,'pagination')
    #    buttun.click()
    #    time.sleep(1)
    element=web.find_elements(By.ID,'report-link')
    sum=0
    for i in element:
        sum+=1
    print(sum)
    f = open("e:/test.csv",'w+',newline='')
    #输出漏洞文章的url
    for i in element:
        writer = csv.writer(f)
        writer.writerow([i.get_attribute('href')])
    f.close()




    '''
    #主页输出内容
    el = web.find_elements(By.XPATH, '/html/body/div[1]/div[1]/div[1]/main[1]/div[3]/div[1]/table/tbody/tr/td/div/div[3]/div[@class="md:text-lg font-bold leading-none"]/a')
    el.click()
    for i in el:
        print(i.text)
    print(el)
	# 点击
    #el.click()                          # "/html/body/div/div[3]/div[1]/div[2]/div[2]/div[2]/div[1]/h4/a"
    # 爬取想要的内容
'''
