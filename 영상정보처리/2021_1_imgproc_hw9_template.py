# -*- coding: utf-8 -*-
"""2021-1-ImgProc-HW9-Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/19kcsy6R26scSAAaB8tY6tSvvMubZsJBj

## 영상정보처리 9주차 과제 템플리트
- 점수: 10점 만점
-- 일부만 찾은 경우 5점, 다 찾으면 10점
- 이미지 경로 잘못 사용한 경우: -3
- 소스 이미지: 
1. messi5.jpg - 샘플 검출 대상 이미지
2. messi5_shirt_blue.png - 셔츠의 파란 부분
3. messi5_shirt_red.png  - 셔츠의 붉은 부분
    

이름: 황예진         
학번: 32195044

# 구글 드라이브 마우팅 및 작업 경로로 이동
- 다음 쉘에 필요한 작업을 하시오.
"""

from google.colab import drive 
drive.mount('/gdrive')

# Commented out IPython magic to ensure Python compatibility.
# %cd /gdrive/My Drive/Classroom/[영상정보처리] 2000004793-2021-1/2021-1 영상정보처리 7강/
import matplotlib.pyplot as plt
import numpy as np
import cv2

"""다음의 경로는 변경하지 말것. 만일 해당 이미지가 없는 경우, 같이 업로드한 이미지를 해당 폴더에 저장해서 사용할 것. """

src_image_path = '../Dongkeun-OpenCV-ImgData/messi5.jpg'
red_roi_image_path = '../Dongkeun-OpenCV-ImgData/messi5_shirt_red.png'
blue_roi_image_path = '../Dongkeun-OpenCV-ImgData/messi5_shirt_blue.png'

## print function
def show_with_matplotlib(img, title):
  """Shows an image using matplotlib capabilities"""

  #Convert BGR image to RGB:
  img_RGB = img[:,:,::-1]
  
  #Show the image using matplotlib:
  plt.imshow(img_RGB)
  plt.title(title)
  plt.show()

def show_with_matplotlib_gray(img, title):
  plt.imshow(img, cmap="gray")
  plt.title(title)
  plt.show()

"""##문제 1:

위에서 언급한 src_image_path 의 이미지 부분 중에서 셔츠 부분을 검출하는 것이 최종 목표이며, 결과 이미지에는 해당 영역의 3-채널 영상 부분이 담겨 있어야 한다. 
방법은 수업 동영상에 설명한 histgram backprojection 을 사용하며, 구체적 단계는 강의 동영상을 참조한다. red_roi_image_path 와 blue_roi_image_path 를 검출 대상에 히스토그램 작성에 사용한다. 





"""

src_image = cv2.imread(src_image_path)  #background image
hsvt = cv2.cvtColor(src_image, cv2.COLOR_BGR2HSV)

red_image = cv2.imread(red_roi_image_path)  #red part
red_hsv = cv2.cvtColor(red_image, cv2.COLOR_BGR2HSV)
roihist1 = cv2.calcHist([red_hsv], [0,2], None, [180, 256], [0, 180, 0, 255])

#plt.title('Histogram for Hue and Saturation')
#plt.ylim(0, 31)
#plt.imshow(roihist1, interpolation = "nearest")
#plt.show()

## normalize histogram and apply backprojection
cv2.normalize(roihist1, roihist1, 0, 255, cv2.NORM_MINMAX)
dst1 = cv2.calcBackProject([hsvt], [0, 2], roihist1, [0, 180, 0, 255], 2)
#show_with_matplotlib_gray(dst1, "BackProjected Image")

## create a disc representing ellipse
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cv2.filter2D(dst1, -1, disc, dst1)
#show_with_matplotlib_gray(dst1, "Filtered Image")

## threshold
ret, thresh = cv2.threshold(dst1,50,255,0)

## threshold and binary AND
thresh3ch = cv2.merge((thresh,thresh,thresh))
res_r = cv2.bitwise_and(src_image, thresh3ch)

show_with_matplotlib(res_r, 'Result')

blue_image = cv2.imread(blue_roi_image_path)  #blue part
blue_hsv = cv2.cvtColor(blue_image, cv2.COLOR_BGR2HSV)

# calculating object histogram
roihist2 = cv2.calcHist([blue_hsv], [0,1], None, [180, 256], [0, 180, 0, 255])

## visualize the 2 channel histogram
#plt.title('Histogram for Hue and Saturation')
#plt.ylim(0, 31)
#plt.imshow(roihist2, interpolation = "nearest")
#plt.show()

## normalize histogram and apply backprojection
cv2.normalize(roihist2, roihist2, 0, 255, cv2.NORM_MINMAX)
dst2 = cv2.calcBackProject([hsvt], [0, 1], roihist2, [0, 180, 0, 255], 1)
#show_with_matplotlib_gray(dst2, "BackProjected Image")

## create a disc representing ellipse
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cv2.filter2D(dst2, -1, disc, dst2)
#show_with_matplotlib_gray(dst2, "Filtered Image")

## threshold
ret, thresh = cv2.threshold(dst2,50,255, 0)
thresh3ch = cv2.merge((thresh,thresh,thresh))
res_b = cv2.bitwise_and(src_image, thresh3ch)
show_with_matplotlib(res_b, 'Result')

# bitwise OR
result_image = cv2.bitwise_or(res_r, res_b)
show_with_matplotlib(result_image, 'Result Image')