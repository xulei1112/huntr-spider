from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time
import csv
if __name__ == '__main__':
    #跳转到github爬取修复代码
    a= open("e:/test2.csv",'r')
    reader=csv.reader(a)
    rows=[row for row in reader]
    for j in rows:
        print(j[5])
        tt=j[5]
        web2= Chrome()
        web2.get(tt)
        #漏洞代码
        #修复代码
        new_code=web2.find_element(By.CSS_SELECTOR,'#files > div.js-diff-progressive-container')
        print(new_code.text)
