from pprint import pprint
import json
import os
from KeyMojiAPI import KeyMoji
import re


dirPath_google = r"C:/Users/USER/Desktop/total_data/each_rest/google"
shop_name_google = os.listdir(dirPath_google)
for i in range(len(shop_name_google)):
    shop_name_google[i] = re.sub(".json","",shop_name_google[i])
    
dirPath_ptt = r"C:/Users/USER/Desktop/total_data/each_rest/PTT"
shop_name_ptt = os.listdir(dirPath_ptt)
for i in range(len(shop_name_ptt)):
    shop_name_ptt[i] = re.sub(".json","",shop_name_ptt[i])
    
dirPath_dcard = r"C:/Users/USER/Desktop/total_data/each_rest/Dcard"
shop_name_dcard = os.listdir(dirPath_dcard)
for i in range(len(shop_name_dcard)):
    shop_name_dcard[i] = re.sub(".json","",shop_name_dcard[i])    
    
for i in range(len(shop_name_google)) :
    temp = []
    f = open('C:/Users/USER/Desktop/total_data/each_rest/google/'+shop_name_google[i]+'.json',encoding='utf-8-sig')
    data = json.load(f)
    for a in range(len(data['reviews'])) :
        temp.append(data['reviews'][a])
    for j in range(len(shop_name_ptt)) :
        if shop_name_google[i] == shop_name_ptt[j] :
            f = open('C:/Users/USER/Desktop/total_data/each_rest/PTT/'+shop_name_ptt[j]+'.json',encoding='utf-8-sig')
            data2 = json.load(f)
   
            for a in range(len(data2['reviews'])) :
                temp.append(data2['reviews'][a])
    for k in range(len(shop_name_dcard)) :
        if shop_name_google[i] == shop_name_dcard[k] :
            f = open('C:/Users/USER/Desktop/total_data/each_rest/Dcard/'+shop_name_dcard[k]+'.json',encoding='utf-8-sig')
            data3 = json.load(f)

            for a in range(len(data3['reviews'])) :
                temp.append(data3['reviews'][a])
                
    data['reviews'] = temp
    
    with open('C:/Users/USER/Desktop/aa/'+shop_name_google[i]+'.json', 'w',encoding='utf8') as f:
            json.dump(data, f, indent=2,ensure_ascii=False)
    
    
    


    
    


