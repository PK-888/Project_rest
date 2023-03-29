import json
import os
import re
from pprint import pprint

from KeyMojiAPI import KeyMoji

#資料進來

#Google
dirPath = r"C:/Users/USER/Desktop/total_data/comment_data/Dcard"
shop_name = os.listdir(dirPath)
for i in range(len(shop_name)):
    shop_name[i] = re.sub(".json","",shop_name[i])



#建dict
data_dict = {
            'name' : '',
            'rate' : '',
            'address' : '',
            "restaurant_type":'',
            "reviews": []
            #分類後才知道    "classrate":''
    }
    #每則評論 reviews SRC=single comment rate
inner_comment = {
            "comment": '',
            "rate": '',
            "resource": '',
            #分類後才知道 "type":'',
            "singlecomment":'',
            "SCR":''   
    }

keymoji = KeyMoji(username="kobejames5566@gmail.com", keymojiKey="NLBilwn-MAe*%2u#GAMn15#CX$3m2-P")


for i in range(len(shop_name)):
    temp = shop_name[i]
    f = open('C:/Users/USER/Desktop/total_data/comment_data/Dcard/'+temp+'.json',encoding='utf-8-sig')
    data = json.load(f)
    #print('第'+str(i)+'間')
    
    #進reviews的list
    toReviews = []

    #innercomment兩個值以上的變數
    toInnerSC = []
    toInnerSCR = []

    
    times = len(data["comment"])
    for j in range(len(data["comment"])):
        inner_comment = {
            "comment": '',
            "rate": '',
            "resource": '',
            #分類後才知道 "type":'',
            "singlecomment":'',
            "SCR":''     
        }
        toSep_dict = {
        "comment" : ''
        }
        #print('第'+str(j)+'則')
        inputSTR = data['comment'][j]
        print(inputSTR)
        #print(inputSTR)
        inner_comment['comment'] = inputSTR
        inner_comment['resource']='PTT'
        try :
            if inputSTR!='None':
                result = keymoji.sense2(inputSTR)
                score = 0
                for k in range(len(result['results'])):
                    score = score + result['results'][k]['score']
                    toInnerSC.append(result['results'][k]['input_str'])
                    toInnerSCR.append((result['results'][k]['score'])*2.5+2.5)
                inner_comment['rate'] = (score/len(result['results']))*2.5+2.5
                inner_comment['singlecomment'] = toInnerSC
                inner_comment['SCR'] = toInnerSCR
                
                toInnerSC = []
                toInnerSCR = []
                toReviews.append(inner_comment)
        except :
            continue   
    data_dict['reviews']=toReviews
    data_dict['name']=shop_name[i]
    rate_ = 0
    for x in range(len(data_dict['reviews'])):
        rate_ = rate_ + data_dict['reviews'][x]['rate']
    if times != 0 :
        data_dict['rate'] = rate_/times
    #建檔

    with open('C:/Users/USER/Desktop/total_data/each_rest/Dcard/'+shop_name[i]+'.json', 'w',encoding='utf8') as f:
            json.dump(data_dict, f, indent=2,ensure_ascii=False)
    
            
