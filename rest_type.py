from pprint import pprint
import json
import os
from KeyMojiAPI import KeyMoji
import re
import pandas as pd
import math


dirPath = r"C:/Users/USER/Desktop/total_data/each_rest/google"
shop_name = os.listdir(dirPath)
for i in range(len(shop_name)):
    shop_name[i] = re.sub(".json","",shop_name[i])


df = pd.read_csv('C:/Users/USER/Desktop/total_data/Restaurant_type/restaurantType.csv',encoding='utf-8-sig')

for i in range(len(shop_name)) :
    for j in range(len(df['name'])) :
        if shop_name[i] == df['name'][j] :
            f = open('C:/Users/USER/Desktop/total_data/each_rest/google/'+shop_name[i]+'.json',encoding='utf-8-sig')
            data = json.load(f)
            data['restaurant_type'] = math.floor(df['type'][j])

            with open('C:/Users/USER/Desktop/aaaa2/'+shop_name[i]+'.json', 'w',encoding='utf8') as f:
                json.dump(data, f, indent=2,ensure_ascii=False)
        