#作者：玉降
#功能：导出总结性pdf报告
import markdown as mk
import pdfkit as pdf
import os

#markdown转HTML表格文本
def change_table(mark):
    out_table = mk.markdown(mark,output_format='html',extensions=['tables'])
    return out_table

#markdown转HTML一般文本
def change_txt(mark):
    out_table = mk.markdown(mark,output_format='html')
    return out_table
#读入封面配置
def load_titlepage(name_,class_,id_,category_name):
    with open('./style/cover.html', 'r', encoding='utf-8') as file:
        html_content = file.read()
    file.close()
    modified_content = html_content.replace('标题',category_name+"实验报告")
    html_content = modified_content
    modified_content = html_content.replace('班级：','班级：{}'.format(class_))
    html_content = modified_content  
    # print(html_content)
    modified_content = html_content.replace('学号：', '学号：{}'.format(id_))
    html_content = modified_content
    modified_content = html_content.replace('姓名：', '姓名：{}'.format(name_))
    # print(modified_content)
    # time.sleep(3600)
    return modified_content


def output_pdf(score_jsons,name_,class_,id_):
    entire = ""
    #报告表格表头
    head1 = "|关卡|任务名称|开启时间|代码修改行数|测评次数|完成时间|实训耗时|是否查看答案|得分|\n|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|:-:|\n"

    # 创建配置对象和css文件
    configuration = pdf.configuration(wkhtmltopdf='./wkhtmltopdf/bin/wkhtmltopdf.exe')
    css = "./style/output_pdf.css"



    filepath = "./OUT/"
    if not os.path.exists(filepath):
        os.makedirs(filepath.encode('utf-8'))
        print('目录'+filepath +'创建成功')

    for a in range(len(score_jsons)):
        category_name = score_jsons[a][0]["category"]["category_name"]      # 实验名称
        output = load_titlepage(name_,class_,id_,category_name)
        body= ""                                                            #输出各项实验的值
        head_table = ""                                                     #实验总量统计
        total_task = 0.001                                                      #总计题目量
        finished_task = 0                                                   #完成题目量
        total_score = 0.001                                                     #总计分数
        get_score = 0                                                       #获得分数
        for b in range(len(score_jsons[a])):
            score_json = score_jsons[a][b]
            if(len(score_json["shixun_detail"]) != 0):
                shixun_name = score_json["shixun_name"]                     # 实训名称
                body = body + change_txt("##"+shixun_name)
                # print(shixun_name)
                stage_list = score_json["stage_list"]                       # 实训详情
                # print(shixun_detail[0])

                table = head1
                task = 0
                fin = 0
                score = 0
                total_score += 100
                for c in range(len(stage_list)):
                    task+=1
                    record = "|{}|{}|{}|{}|{}|{}|{}|{}|{}|\n".format(c,stage_list[c]["name"],stage_list[c]["open_time"],stage_list[c]["diff_code_count"],stage_list[c]["evaluate_count"],stage_list[c]["finished_time"],stage_list[c]["time_consuming"],stage_list[c]["view_answer"],stage_list[c]["game_score"])
                    if(stage_list[c]["finished_time"]!="--"):
                        fin+=1
                    table = table+record
                score = round(100*fin/task,1)
                body = body+change_table(table)+"<table><tbody><tr><td>题目完成情况</td><td>{}/{}</td><td>题目完成率</td><td>{}%</td><td>得分</td><td>{}</td></tr></tbody><colgroup><col style=\"width: 14.2222%;\"><col style=\"width: 19.1111%;\"><col style=\"width: 13.1111%;\"><col style=\"width: 20.2222%;\"><col style=\"width: 9.20833%;\"><col style=\"width: 24.125%;\"></colgroup></table>".format(fin,task,round(fin/task*100),score)
                total_task += task
                finished_task += fin
                get_score += score
        head_table = "<table><tbody><tr><td>题目完成情况</td><td>{}/{} </td><td>题目完成率</td><td>{}%</td><td>总分</td><td>{}</td><td>平均分</td><td>{}</td></tr></tbody><colgroup><col style=\"width: 13.4444%;\"><col style=\"width: 10.2222%;\"><col style=\"width: 11.3333%;\"><col style=\"width: 9.22222%;\"><col style=\"width: 9.22222%;\"><col style=\"width: 13.8889%;\"><col style=\"width: 12.8889%;\"><col style=\"width: 19.6667%;\"></colgroup></table>".format(round(finished_task,1),round(total_task,1),round(finished_task/total_task*100,1),round(get_score),round(get_score/total_score*100))
        # 生成报告pdf
        output = output +head_table
        output = output + body
        pdf.from_string(output, output_path=filepath+category_name+"实验报告.pdf", configuration=configuration, options={'encoding': 'utf-8'},css=css)
        entire = entire + "<div style=\"page-break-before: always;\">{}</div>".format(output)
    with open('./style/end.html', 'w', encoding='utf-8') as file:
        file.write(entire)
    file.close()
    pdf.from_string(entire, output_path="./OUT/实验报告(everything).pdf", configuration=configuration, options={'encoding': 'utf-8'},css=css)    
