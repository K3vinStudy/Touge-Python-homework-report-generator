# name: 获取作业源代码（educoder）
# 作者：K3vin
import os

def getCode(score_jsons):
    print('')
    for a in range(len(score_jsons)):
        category_name = score_jsons[a][0]["category"]["category_name"]                      # 实验名称
        for b in range(len(score_jsons[a])):    # 获取项目json
            score_json = score_jsons[a][b]
            
            # 分项目生成文件
            if(len(score_json["shixun_detail"]) != 0):      # 判断有没有做，没做直接跳过
                # 生成文件名和路径
                shixun_name = score_json["shixun_name"]                                     # 实训名称
                # print(shixun_name)
                filepath = "OUT/source/"+category_name+"/"+shixun_name+"/"
                
                # 创建目录
                if not os.path.exists(filepath):
                    os.makedirs(filepath.encode('utf-8'))
                    print('目录 “'+filepath +'” 创建成功')
                
                # 生成源代码文件
                shixun_detail = score_json["shixun_detail"]                                 # 实训详情
                # print(shixun_detail[0])
                for c in range(len(shixun_detail)):
                    filename = str(shixun_detail[c]["position"])+".py"
                    code = shixun_detail[c]["game_codes"][0]["content"]        
                    with open(filepath+filename, 'w', encoding='utf-8') as file:
                        file.write(code)
    
    