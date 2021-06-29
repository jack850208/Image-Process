# -*- coding: utf-8 -*-
"""
Created on Thu Jun  3 15:29:04 2021

@author: AIC
"""

import scipy.io as matlab
import matplotlib.pyplot as plt 

dig = matlab.loadmat(r'D:\109 Master Jack\嵌入式影像處理\IC量測資料\mat檔\TDC_temp_resolution.mat')
res = matlab.loadmat(r'D:\109 Master Jack\嵌入式影像處理\IC量測資料\mat檔\TDC_dig.mat')

chip1_reg = dig['chip1_reg'][0]
chip2_reg = dig['chip2_reg'][0]
chip3_reg = dig['chip3_reg'][0]
chip_digita1 = dig['chip_digita1'][0]
chip_digita2 = dig['chip_digita2'][0]
chip_digita3 = dig['chip_digita3'][0]
temp_range = dig['x2'][0]

# chip1_digita1 diff
chip_diff1 = []
chip_diff2 = []
chip_diff3 = []
for index in chip_digita1:
    chip_diff1.append(index[0][-1]-index[0][0])
for index in chip_digita2:
    chip_diff2.append(index[0][-1]-index[0][0])
for index in chip_digita3:
    chip_diff3.append(index[0][-1]-index[0][0])

# show Temp to Digital value
fig1, p1 = plt.subplots()
fig1.suptitle('Temp to Digital')
p1.set_xlabel('Temp')
p1.set_ylabel('Digital')
p1.plot(temp_range, chip_diff1)
p1.plot(temp_range, chip_diff2)
p1.plot(temp_range, chip_diff3)




"""
plt.plot(temp_range, chip1_reg)
plt.plot(temp_range, chip2_reg)
plt.plot(temp_range, chip3_reg)
plt.xlabel('Temp(C)')
plt.ylabel('resolution(ns)')
"""


# plt.savefig('fig.png')