# 头歌爬虫主程序（educoder）
import get_cookie
import getData
import getCode
import filesCode
import time

if __name__=="__main__":
    # 登录并获取cookie
    get_cookie.get_cookie()
    time.sleep(0.5)
    
    # 输入姓名、班级、学号
    print("\n以下信息用于生成实验报告")
    name = input('请输入姓名:')
    clas = input('请输入班级:')
    id = input('请输入学号:')
    
    # 选择生成作业或实验
    while True:
        choice = int(input('\n请选择要生成的内容\n1.生成作业练习\n2.生成实验项目\n在此输入序号选择: '))
        if choice == 1:
            choice = 0
            print("\n正在生成作业练习...\n")
            break
        if choice == 2:
            choice = 1
            print("\n正在生成实验项目...\n")
            break
        else:
            print("\n输入错误,请重新输入!\n")
    
    # 获取所有json内容
    score_jsons = getData.getData(choice)
    
    # 生成报告PDF和源代码文件
    getCode.getCode(score_jsons)
    filesCode.output_pdf(score_jsons, name, clas, id)
    print("\n生成完毕,请查看OUT文件夹!\n")
    
