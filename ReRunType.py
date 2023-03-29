from pprint import pprint
import json
import os
from KeyMojiAPI import KeyMoji
import re
import pandas as pd
import math



dirPath = r"C:/Users/USER/Desktop/ReGoogle"
shop_name = os.listdir(dirPath)

list_=[]
less_one = 0
one_to_two = 0
two_to_three = 0
bigger = 0

for i in range(len(shop_name)):
    f = open('C:/Users/USER/Desktop/ReGoogle/'+shop_name[i],encoding='utf-8-sig')
    data = json.load(f)
    list_.append(data['rate'])
    if data['rate'] < 1 :
        less_one = less_one +1
    if 1 < data['rate'] < 2 :
        one_to_two = one_to_two + 1
    if 2 < data['rate'] < 3 :
        two_to_three = two_to_three + 1
    if data['rate'] > 3 :
        bigger = bigger + 1
    
#print(less_one,one_to_two,two_to_three,bigger)
print(max(list_))