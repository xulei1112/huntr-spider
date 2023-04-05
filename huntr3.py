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

        with open('e:/test2.csv','a',newline='') as result:
            writer=csv.writer(result)
            writer.writerow([j[0],ele[0],ele[4],aa,bb])
