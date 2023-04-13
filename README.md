![huntr-spider](https://socialify.git.ci/xulei1112/huntr-spider/image?font=Source%20Code%20Pro&language=1&logo=https%3A%2F%2Favatars.githubusercontent.com%2Fu%2F64565724%3Fv%3D4&name=1&pattern=Overlapping%20Hexagons&theme=Dark)
# huntr-spider
默认输入输出路径均为e盘，需要提前修改自己实际路径
geckodriver与chorm驱动需要根据自己电脑浏览器的实际版本修改，具体可以百度，我这里提供的是适合我自己电脑浏览器版本的驱动

huntr1.py用来从huntr网站（https://huntr.dev/ ）
爬取漏洞文章链接
![image](https://user-images.githubusercontent.com/64565724/230029991-d921541a-cb6b-4e0d-92f3-b75fc11c6fc0.png)

![image](https://user-images.githubusercontent.com/64565724/230029555-6a63c661-de7a-4e9f-bf03-93e0c3b7d55c.png)


huntr2.py用来访问漏洞文章，是个过度脚本
huntr3.py用来爬取漏洞文章中的Description、title、CVE、CWE等信息
![image](https://user-images.githubusercontent.com/64565724/230030070-832e9354-9f04-47fd-8faa-16ada760f4ea.png)
![image](https://user-images.githubusercontent.com/64565724/230030415-602f7d7d-8d08-4609-bae6-3e7c35085cef.png)
huntr4.py用来爬取github中的漏洞修复代码与漏洞代码
![image](https://user-images.githubusercontent.com/64565724/230030662-6b583475-6054-4b1d-bd29-6eda44765459.png)
此项目可以作为漏洞数据集等利用，用于漏洞研究与科研等
![image](https://user-images.githubusercontent.com/64565724/230545240-b1cf7718-c70f-41c4-bf00-5826c2373364.png)
有较好的反爬虫效果

huntr5.py用来爬取指定代码类型的（比如C语言），换成火狐浏览器驱动，防止内存溢出，导致无法大量爬取数据
![image](https://user-images.githubusercontent.com/64565724/231638855-715182f1-6b4e-4d1f-8d7d-770a70279179.png)

