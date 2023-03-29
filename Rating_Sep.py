from pprint import pprint
import json
import os
from KeyMojiAPI import KeyMoji
import re

#資料進來

#Google
dirPath = r"C:/Users/USER/Desktop/total_data/comment_data/Google"
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
            "SCR":'' ,
            "type": ''     
    }

keymoji = KeyMoji(username="kobejames5566@gmail.com", keymojiKey="NLBilwn-MAe*%2u#GAMn15#CX$3m2-P")

y = 168
for i in range(len(shop_name)):
    temp = shop_name[y]
    f = open('C:/Users/USER/Desktop/total_data/comment_data/Google/'+temp+'.json',encoding='utf-8-sig')
    data = json.load(f)
    #print('第'+str(i)+'間')
    
    #進reviews的list
    toReviews = []

    #innercomment兩個值以上的變數
    toInnerSC = []
    toInnerSCR = []

    #每句拆開的dict
    SepComment = {
        "comment" :''
    }
    #丟進SepComment的list
    toSep_list = []
    
    sep_comment = []
    times = len(data)
    for j in range(len(data)):
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
        inputSTR = data[str(j)]['comment']
        #print(inputSTR)
        inner_comment['comment'] = inputSTR
        inner_comment['resource']='Google'
        try :
            if inputSTR!='None':
                result = keymoji.sense2(inputSTR)
                score = 0
                for k in range(len(result['results'])):
                    score = score + result['results'][k]['score']
                    toInnerSC.append(result['results'][k]['input_str'])
                    sep_comment.append(result['results'][k]['input_str']) #sep comment
                    toInnerSCR.append((result['results'][k]['score'])*2.5+2.5)
                inner_comment['rate'] = (score/len(result['results']))*2.5+2.5
                inner_comment['singlecomment'] = toInnerSC
                inner_comment['SCR'] = toInnerSCR
                toSep_dict['comment'] = sep_comment #sep
                
                toInnerSC = []
                sep_comment = []
                toInnerSCR = []
                toReviews.append(inner_comment)
                toSep_list.append(toSep_dict) #sep
        except :
            continue
    print('結尾')    
    data_dict['reviews']=toReviews
    data_dict['name']=shop_name[i]
    rate_ = 0
    for x in range(len(data_dict['reviews'])):
        rate_ = rate_ + data_dict['reviews'][x]['rate']
    if times != 0 :
        data_dict['rate'] = rate_/times
    SepComment['comment'] = toSep_list #sep       
    pprint(SepComment)
    #建檔

    with open('C:/Users/USER/Desktop/total_data/each_rest/google/'+shop_name[y]+'.json', 'w',encoding='utf8') as f:
            json.dump(data_dict, f, indent=2,ensure_ascii=False)


    with open('C:/Users/USER/Desktop/total_data/sep_com/'+shop_name[y]+'.json', 'w',encoding='utf8') as f:
            json.dump(SepComment, f, indent=2,ensure_ascii=False)     
    
    y = y + 1
            
