from pprint import pprint
from KeyMojiAPI import KeyMoji
import os
from matplotlib.font_manager import json_load
import json
from ArticutAPI import Articut

#declare
score = []


#Get shopname--------------------------------------------------------------------------
dirPath = r"C:/Users/USER/Desktop/data/222/restaurants1.0_json"
shop_name = os.listdir(dirPath)

characters = ".json"
total_shopname = []

for i in range(len(shop_name)) :
    shop_name[i] = ''.join( x for x in shop_name[i] if x not in characters)
    total_shopname.append(shop_name[i])


#Get comment----------------------------------------------------------------------------
for shop in total_shopname :
    f = open('C:/Users/USER/Desktop/data/新增資料夾/restaurants1.0_json/'+shop+'.json',encoding='utf-8-sig')
    data = json.load(f)

    tem_score = 0
    #score--------------
    for i in range(len(data)-1) : 
        keymoji = KeyMoji(username="", keymojiKey="")

        inputSTR = data[str(i)]['comment']
        if inputSTR == 'None' :
            continue
        result = keymoji.sense2(inputSTR)
        

        for i in range(len(result['results'])) :
            tem_score =tem_score + result['results'][i]["score"]
            
    score.append(tem_score)
    
    #menu---------------
    for i in range(len(data)-1) : 
        articut = Articut(username="", apikey="")

        inputSTR = data[str(i)]['comment']
        if inputSTR == 'None' :
            continue
        resultDICT = articut.parse(inputSTR)
        
        foodLIST = articut.NER.getFood(resultDICT)
        restfood = []
        for food in foodLIST :
            if food == "" :
                continue
        
            restfood.append(food)
    