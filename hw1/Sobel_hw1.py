# coding=utf-8
import cv2
import numpy as np

img = cv2.imread('1200px-Road_in_Norway.jpg', 0)

'''
在Sobel函式的第二個引數這裡使用了cv2.CV_16S。
因為OpenCV文件中對Sobel運算元的介紹中有這麼一句：
“in the case of 8-bit input images it will result in truncated derivatives”。
即Sobel函式求完導數後會有負值，還有會大於255的值。
而原影象是uint8，即8位無符號數，所以Sobel建立的影象位數不夠，會有截斷。
因此要使用16位有符號的資料型別，即cv2.CV_16S。

在經過處理後，別忘了用convertScaleAbs()函式將其轉回原來的uint8形式。
否則將無法顯示影象，而只是一副灰色的視窗。convertScaleAbs()的原型為：
dst = cv2.convertScaleAbs(src[, dst[, alpha[, beta]]])

其中可選引數alpha是伸縮係數，beta是加到結果上的一個值。結果返回uint8型別的圖片。
由於Sobel運算元是在兩個方向計算的，最後還需要用cv2.addWeighted(...)函式將其組合起來。
其函式原型為：
dst = cv2.addWeighted(src1, alpha, src2, beta, gamma[, dst[, dtype]])
其中alpha是第一幅圖片中元素的權重，beta是第二個的權重，gamma是加到最後結果上的一個值。
'''

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)# 轉回uint8
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow("orign", img)
cv2.imshow("absX", absX)
cv2.imshow("absY", absY)

cv2.imshow("Result", dst)

cv2.imwrite('hw1/gray.jpg',img)
cv2.imwrite('hw1/absX.jpg',absX)
cv2.imwrite('hw1/absY.jpg',absY)
cv2.imwrite('hw1/Result.jpg',dst)

cv2.waitKey(0)
cv2.destroyAllWindows()