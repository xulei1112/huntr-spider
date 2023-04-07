from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import csv

if __name__ == '__main__':
    a= open("e:/test.csv",'r')
    reader=csv.reader(a)
    rows=[row for row in reader]
    #从csv文件中取出url链接，然后使用爬虫进行访问获取
    for j in rows:
        print(j[0])
        web = Chrome()
        #打开test2.csv准备把爬取内容存入其中
        web.get(j[0])
        #下面的element是爬取wp内容的
        element=web.find_element(By.ID,'write-up')
        #截取Description内容，匹配Proof of Concept或者impact之前的内容输出
        ele=element.text.split('\n')
        #print(ele[0])
        #print(ele[4])
        #下面的cve是爬取cve与CWE内容的
        cve=web.find_element(By.ID,'meta-container')
        l=cve.text.split('\n')
        aa=''
        bb=''
        for i in l:
            if "CVE-" in i:
                #print(i)
                aa=i

            if "CWE" in i:
                #print(i)
                bb=i
        #tt是定位github的修复代码链接
        tt=web.find_element(By.CSS_SELECTOR,'#message-box > div.text-sm.font-medium.w-full.mt-1 > div:nth-child(1) > div.inline-block.self-center.mx-2 > a.break-words.hover\:text-blue-400.hover\:underline')
        #print(tt.get_attribute('href'))
        web2= Chrome()
        #访问github链接
        web2.get(tt.get_attribute('href')+'?diff=split')
        #获取修复代码#files > div.js-diff-progressive-container
        ff=""
        #正则表达式匹配
        old_code=web2.find_elements(By.XPATH,'//*[@data-details-container-group="file"]/div[2]/div/table/tbody/tr/td[2]')
        for i in old_code:
            ff+=i.text+'\n'

        web3=Chrome()
        web3.get(tt.get_attribute('href')+'?diff=unified')
        new_code=web3.find_element(By.CSS_SELECTOR,'#files > div.js-diff-progressive-container')
        with open('e:/test3.csv','a+',newline='',encoding='utf-8') as result:
            writer=csv.writer(result)
            writer.writerow([j[0],ele[0],ele[4],aa,bb,tt.get_attribute('href'),ff,new_code.text])
