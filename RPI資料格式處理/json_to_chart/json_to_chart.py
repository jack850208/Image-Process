# -*- coding: utf-8 -*-
"""
Created on Fri May 28 12:17:19 2021

@author: AIC
"""

import matplotlib.pyplot as plt
import json

# load json file
fp = open(r"excel_to_json.json","r")
load_json = json.load(fp)
fp.close()

ic_data = []
cnt = 0
cnt_flag = 0

# create container
for index in range(len(load_json.keys())):
    ic_data.append([])
    
for item in load_json.keys():
    if(cnt_flag != 0): cnt = cnt + 1
    cnt_flag = cnt_flag + 1
    for item2 in load_json[item].keys():
        ic_data[cnt].append(load_json[item][item2])

plt.plot(ic_data[0][1:], ic_data[1][1:])
plt.plot(ic_data[0][1:], ic_data[2][1:])
plt.xlabel("Temp")
plt.ylabel("Digital value")
plt.show()