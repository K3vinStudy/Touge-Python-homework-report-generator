# name: 获取作业URL（educoder）
# 作者：K3vin
import json
import time
import os

import getResp

def getData(choice):
    # 获取个人空间ID
    responseText = getResp.get_json_withCookie('https://data.educoder.net/api/users/get_user_info.json?school=1')
    zzud = responseText['login']
    
    # 获取课程ID
    responseText = getResp.get_json_withCookie('https://data.educoder.net/api/users/'+zzud+'/courses.json?category=&status=&page=1&per_page=200&sort_by=updated_at&sort_direction=desc&username='+zzud+'&zzud='+zzud)
    courses = responseText['courses']
    for i in range(len(courses)):
        if courses[i]['name'] == 'Python程序设计-22网工':                           # 课程名称
            first_category_url = courses[i]['first_category_url']
            courseId = os.path.split(os.path.split(first_category_url)[0])[1]
            break
    
    # 获取实验作业ID
    responseText = getResp.get_json_withCookie('https://data.educoder.net/api/courses/'+courseId+'/left_banner.json?id='+courseId+'&zzud='+zzud)
    second_category = responseText['course_modules'][0]['second_category']
    
    category_ids = []
    for i in range(0, 9):
        category_ids.append(second_category[i*2+choice]['category_id'])             # 截取实验或作业ID
    
    # 获取所有json内容
    results = []
    
    for a in range(0, len(category_ids)):
        print("正在获取第("+str(a+1)+"/"+str(len(category_ids))+")个实验作业的信息...")
        responseText = getResp.get_json_withCookie('https://data.educoder.net/api/courses/'+courseId+'/homework_commons.json?limit=100&status=0&id='+courseId+'&type=4&category='+json.dumps(category_ids[a])+'&page=1&order=0&zzud='+zzud)
        homeworks = responseText['homeworks']
        
        score_jsons = []
        # score_urls = []
        for b in range(0, len(homeworks)):
            # 获取项目ID
            categoryId = json.dumps(homeworks[b]['homework_id'])
            homeworkId = json.dumps(homeworks[b]['student_work_id'])           
            
            # 获取总评页面url
            score_url='https://data.educoder.net/api/student_works/'+homeworkId+'/shixun_work_report.json?coursesId='+courseId+'&categoryId='+categoryId+'&homeworkId='+homeworkId+'&zzud=mkh5xyn9g'
            # score_urls.append(score_url)
            # print(score_url)
            
            # 获取总评页面json
            responseText = getResp.get_json_withCookie(score_url)
            score_jsons.append(responseText)
            time.sleep(0.2)       # 休眠0.618秒，控制速度
        
        # results.append(score_urls)
        print('成功获取'+str(len(score_jsons))+'项实训信息!')
        time.sleep(0.5)
        # with open('example'+str(a)+'.json', 'w', encoding='utf-8') as file:
        #     file.write(json.dumps(score_jsons))
        results.append(score_jsons)
    
    os.remove('cookie.txt')
    print("\ncookie已删除")
    return results
    
        

