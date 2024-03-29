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
        try:
            element=web.find_element(By.XPATH,'//*[@id="markdown"]/span/p[1]')
        except:
            element=web.find_element(By.XPATH,'//*[@id="title"]')
        #截取Description内容

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
        try:
            tt=web.find_element(By.CSS_SELECTOR,'#message-box > div.text-sm.font-medium.w-full.mt-1 > div:nth-child(1) > div.inline-block.self-center.mx-2 > a.break-words.hover\:text-blue-400.hover\:underline')
        except:                                  
            tt=web.find_element(By.CSS_SELECTOR,'#message-box > div.text-sm.font-medium.w-full.mt-1 > div:nth-child(1) > div.inline-block.self-center.mx-2 > a.break-words.hover\:text-blue-400.hover\:underline')
        #print(tt.get_attribute('href'))
        web2= Chrome()
        #访问github链接
        aaa=tt.get_attribute('href')+"?diff=split"
        print(aaa)
        web2.get(aaa)
        #获取修复代码#files > div.js-diff-progressive-container

        #正则表达式匹配
        ff=""
        tt=""
        old_code=web2.find_elements(By.XPATH,'//*[@data-details-container-group="file"]/div[2]/div/table/tbody/tr/td[2]')
        for i in old_code:
            if "@@" in i.text:
                tt+=i.text[i.text.rfind('@@')+2::]+'\n'
                continue
            else:
                tt+=i.text+'\n' 
        new_code=web2.find_elements(By.XPATH,'//*[@data-details-container-group="file"]/div[2]/div/table/tbody/tr/td[4]')
        for i in new_code:
            ff+=i.text+'\n'
        with open('e:/test3.csv','a+',newline='',encoding='gb18030') as result:
            writer=csv.writer(result)
            writer.writerow([element.text,aa,bb,tt,ff,j[0]])
