from pprint import pprint
from KeyMojiAPI import KeyMoji
import os
from matplotlib.font_manager import json_load
import json
from ArticutAPI import Articut


#Get shopname--------------------------------------------------------------------------
dirPath = r"C:/Users/USER/Desktop/data/222/restaurants1.0_json"
shop_name = next(os.walk(dirPath))

shop_name = list(shop_name)
characters = ".json"


"""for i in range(len(shop_name)) :
    shop_name[i] = ''.join( x for x in shop_name[i] if x not in characters)
    total_shopname.append(shop_name[i])"""
shop_list = shop_name[2]
pprint(shop_list)
  
for i in range(4) :
    temp = shop_list[i+236]
    f = open('C:/Users/USER/Desktop/data/222/restaurants1.0_json/'+temp,encoding='utf-8-sig')
    data = json.load(f)
    restfood = []
    #menu---------------
    for i in range(len(data)-1) : 
        articut = Articut(username="kobejames5566@gmail.com", apikey="9XX75XiIR%j$AL-6$-A_IbH1Vuv=zm2")

        inputSTR = data[str(i)]['comment']
        if inputSTR == 'None' :
            continue
        resultDICT = articut.parse(inputSTR)
        
        foodLIST = articut.NER.getFood(resultDICT)
        if foodLIST is not None :    
            for food in foodLIST :
                for word in food :
                    restfood.append(word[-1])
        else :
            print('skip')
            
    with open('C:/Users/USER/Desktop/newjson/'+temp, 'w',encoding='utf8') as f:
        json.dump(restfood, f, indent=2,ensure_ascii=False)