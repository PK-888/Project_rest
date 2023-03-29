import json
import os
import time
from pprint import pprint

from KeyMojiAPI import KeyMoji


def aver(list_) :
    aver = sum(list_)/len(list_)
    return aver
        


#import data

dirPath = r"C:/Users/USER/Desktop/aa"
shop_name = os.listdir(dirPath) #shopname.json


#re rating
for i in range(len(shop_name)) :
    f = open("C:/Users/USER/Desktop/aa/"+shop_name[i],encoding='utf-8-sig')
    data = json.load(f)
    
    #--------------------存整間店的各項數據分數總合
    class1 = []
    class2 = []
    class3 = []
    class4 = []
    class5 = []
    #-------------------------------
    total = []    #存所有評論的總分
    class_aver = []    #存各個class的平均值
    
    
    for j in range(len(data['reviews'])) : 
        keymoji = KeyMoji(username="kobejames5566@gmail.com", keymojiKey="NLBilwn-MAe*%2u#GAMn15#CX$3m2-P")
        ReScore = []
        singlerate = [0,0,0,0,0]
        count_singlerate = [0,0,0,0,0]
        for k in range(len(data['reviews'][j]['singlecomment'])) :
            inputSTR = data['reviews'][j]['singlecomment'][k]
            
            #rating
            print(inputSTR)
            result = keymoji.sense2(inputSTR)
            pprint(result)           
            score = result['results'][0]['score']
            time.sleep(2)
            
            #classification --------------------------------整間店的各項數據分數總合
            type = data['reviews'][j]['type'][k]
            if type == 1 :
                class1.append(score)
                count_singlerate[0] = count_singlerate[0] + 1
                singlerate[0] = (singlerate[0]+score)/count_singlerate[0]
            if type == 2 :
                class2.append(score)
                count_singlerate[1] = count_singlerate[1] + 1
                singlerate[1] = (singlerate[1]+score)/count_singlerate[1]
            if type == 3 :
                class3.append(score)
                count_singlerate[2] = count_singlerate[2] + 1
                singlerate[2] = (singlerate[2]+score)/count_singlerate[2]
            if type == 4 :
                class4.append(score)
                count_singlerate[3] = count_singlerate[3] + 1
                singlerate[3] = (singlerate[3]+score)/count_singlerate[3]
            if type == 5 :
                class5.append(score)
                count_singlerate[4] = count_singlerate[4] + 1
                singlerate[4] = (singlerate[4]+score)/count_singlerate[4]
            
            #shop rate-------------------------------------整間店全部的分數總合
            total.append(score)
            
            #sent value
            ReScore.append(score)
        
        data['reviews'][j]['SCR'] = ReScore
        for x in range(5) :
            singlerate[x] = float("{:.1f}".format(singlerate[x]))
        data['reviews'][j]['singlerate'] = singlerate
    if class1 != [] :
            class_aver.append(float("{:.1f}".format(aver(class1))))
    else :
        class_aver.append(0)
    if class2 != [] :
        class_aver.append(float("{:.1f}".format(aver(class2))))
    else : 
        class_aver.append(0)
    if class3 != [] :
        class_aver.append(float("{:.1f}".format(aver(class3))))
    else :
        class_aver.append(0)
    if class4 != [] :
        class_aver.append(float("{:.1f}".format(aver(class4))))
    else :
        class_aver.append(0)
    if class5 != [] :
        class_aver.append(float("{:.1f}".format(aver(class5))))
    else :
        class_aver.append(0)
    data['photo'] = ''
    data['popularity'] = ''
    data['class_rate'] = class_aver
    data['rate'] = float("{:.1f}".format(aver(total)))
    
    
    #create data
    with open('C:/Users/USER/Desktop/aaa/'+shop_name[i],'w',encoding='utf-8-sig') as f:
            json.dump(data, f, indent=2,ensure_ascii=False)
            