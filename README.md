# Touge-Python-homework-report-generator
头歌平台Python程序设计作业报告爬虫

使用说明:<br>
wkhtmltopdf用于生成实验报告，需要自己手动从官网下载正确的安装包，安装到源代码内的wkhtmltopdf目录方可使用。<br>
下载地址：https://wkhtmltopdf.org/downloads.html<br>
姓名、班级和学号需要手动输入。报告日期目前写定在2024年1月5日，有需要的朋友可以自行修改filesCode.py和cover.html文件；生成报告的目标课程名也是写死的，即“Python程序设计-22网工”，有其他需要可以自行修改getData.py文件。
<!--有能力的话也可以Pull request到项目里，把它们修改成手动输入的。-->

ps:<br>
本项目使用了requests包，3.9.13以下版本的Python可能会与代理打架导致报错，使用时请暂时关闭代理软件。
