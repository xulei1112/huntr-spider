from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import csv

if __name__ == '__main__':
    path_a='e:\test.csv'
    a= open("e:/test.csv",'r')
    reader=csv.reader(a)
    rows=[row for row in reader]
    #从csv文件中取出url链接，然后使用爬虫进行访问获取
    for i in rows:
        print(i[0])
        web = Chrome()
        web.get(i[0])
        #下面的element是爬取wp内容的
        element=web.find_elements(By.ID,'write-up')
        #截取Description内容，匹配Proof of Concept之前的内容输出
        for i in element:
            if "Concept" in i.text:
                print(i.text[0:i.text.find('Proof of Concept')])
                break
            if "Impact" in i.text:
                print(i.text[0:i.text.find('Impact')])
                break
            else:
                print(i.text)
        #下面的cve是爬取cve内容的
        cve=web.find_element(By.ID,'meta-container')
        l=cve.text.split('\n')
        for i in l:
            if "CVE" in i:
                print(i)
            if "CWE" in i:
                print(i)
