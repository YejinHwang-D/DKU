# -*- coding: utf-8 -*-
"""2021-1-ImgProc-HW10-Template.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1J4G0-HmZOf64baNA8bnVLM0PKsDihfzt

## 영상정보처리 10주차 과제 템플리트
- 마감: 2021년 5월 14일 11시 59분
- 점수: 10점 만점
    
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
import time

image_path = '../Dongkeun-OpenCV-ImgData/leaf.png'
image_path_noised = '../Dongkeun-OpenCV-ImgData/leaf-noise.png'

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

def show_hist_with_matplotlib_gray_modified(hist, title, color, t=-1):
  # ax = plt.subplot(2, 2, pos)
  # plt.title(title)
  plt.xlabel("bins")
  plt.ylabel("number of pixels")
  plt.xlim([0, 256])
  plt.axvline(x=t, color='m', linestyle='--')
  plt.plot(hist, color=color)

"""##문제 1
1. otsu's binarization에서 같이 사용하는 thresholding  방법론 THRESH_BINARY, THRESH_TRUC, THRESH_TOZERO 변경하여 사용 경우, 필터링으로 선작업을 하지 않은 결과에 어떤 영향을 미치는 지, 예시하는 프로그램과 결과를 간단하게 정리하시오. 

2. 또한 위의 분석을 가우시안 필러를 적용했을 때, 어떻게 변화하는 지 예시하는 프로그램과 결과를 간단하게 정리하시오. 

테스트 이미지는 위에서 주어진 image_path, image_path_noised 를 사용하시오. 






"""

## 1. Otsu's binarization 필터링 선작업 X
image1 = cv2.imread(image_path)
image2 = cv2.imread(image_path_noised)
gray_image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
gray_image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)

ret1, th1 = cv2.threshold(gray_image1, 0, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
ret3, th3 = cv2.threshold(gray_image1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret5, th5 = cv2.threshold(gray_image1, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)

show_with_matplotlib(image1, "image1") # 원본 이미지
show_with_matplotlib(cv2.cvtColor(th1, cv2.COLOR_GRAY2BGR), "Otsu trunc")
show_with_matplotlib(cv2.cvtColor(th3, cv2.COLOR_GRAY2BGR), "Otsu binary")
show_with_matplotlib(cv2.cvtColor(th3, cv2.COLOR_GRAY2BGR), "Otsu tozero")

ret1, th1 = cv2.threshold(gray_image2, 0, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
ret3, th3 = cv2.threshold(gray_image2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret5, th5 = cv2.threshold(gray_image2, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)

show_with_matplotlib(image2, "image2") # 원본 이미지
show_with_matplotlib(cv2.cvtColor(th1, cv2.COLOR_GRAY2BGR), "Otsu trunc")
show_with_matplotlib(cv2.cvtColor(th3, cv2.COLOR_GRAY2BGR), "Otsu binary")
show_with_matplotlib(cv2.cvtColor(th3, cv2.COLOR_GRAY2BGR), "Otsu tozero")

#Otsu 방법론에서 BINARY를 사용하면 pixel 값이 value보다 크면 value값으로, 작으면 0으로 설정하므로 
#검은색과 흰색이 명확하게 구분되는 형태로 출력된다. TRUNC를 사용하면 value보다 크면 value 값, 작으면 
#pixel의 원래 값 그대로 설정하므로 원본 이미지와 비슷한 형태로 출력된다. 마지막으로 TOZERO는 value보다
#원래 값 그대로, 작으면 0으로 설정하므로 BINARY와 마찬가지로 대비가 극명하게 출력된다.

## 2. Otsu's binarization 필터링 선작업 O

gray_image_blurred1 = cv2.GaussianBlur(gray_image1, (25, 25), 0) #가우시안 필러
ret1, th1 = cv2.threshold(gray_image_blurred1, 0, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
ret3, th3 = cv2.threshold(gray_image_blurred1, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret5, th5 = cv2.threshold(gray_image_blurred1, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)

show_with_matplotlib(cv2.cvtColor(th1, cv2.COLOR_GRAY2BGR), "1. Gaussian filter TRUNC")
show_with_matplotlib(cv2.cvtColor(th3, cv2.COLOR_GRAY2BGR), "1. Gaussian filter BINARY")
show_with_matplotlib(cv2.cvtColor(th5, cv2.COLOR_GRAY2BGR), "1. Gaussian filter TOZERO")


gray_image_blurred2 = cv2.GaussianBlur(gray_image2, (25, 25), 0) #가우시안 필러
ret1, th1 = cv2.threshold(gray_image_blurred2, 0, 255, cv2.THRESH_TRUNC + cv2.THRESH_OTSU)
ret3, th3 = cv2.threshold(gray_image_blurred2, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
ret5, th5 = cv2.threshold(gray_image_blurred2, 0, 255, cv2.THRESH_TOZERO + cv2.THRESH_OTSU)

show_with_matplotlib(cv2.cvtColor(th1, cv2.COLOR_GRAY2BGR), "2. Gaussian filter TRUNC")
show_with_matplotlib(cv2.cvtColor(th3, cv2.COLOR_GRAY2BGR), "2. Gaussian filter BINARY")
show_with_matplotlib(cv2.cvtColor(th5, cv2.COLOR_GRAY2BGR), "2. Gaussian filter TOZERO")
#가우시안 필터링을 사용하면 노이즈를 효과적으로 제거할 수 있다.
#이 예시에서는 노이즈가 강한 image2에서 효과가 극대로 나타났다.

"""### 문제 2 
위의 노이즈가 있는 영상에 가우시안 필터링을 사용하는 경우, otsu's binarization 과 triangle ninarization 방법론의 성능의 소요 시간을 측정하고, 간단하게 결과를 정리하시오. 시간을 분석할 때는, 필터링 시간은 따로 측정하여, 순수하게 각 방법론에 걸린 시간, 총 시간을 연계하여 분석하시오. 
"""

image = cv2.imread(image_path_noised)
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

## otsu
gray_image_blurred = cv2.GaussianBlur(gray_image, (25, 25), 0)  #가우시안 필터링
start_time = time.time() #시간 측정 시작
ret1, th1 = cv2.threshold(gray_image_blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
end_time = time.time() #시간 측정 종료

print("otsu's time : ", end_time - start_time)
show_with_matplotlib(cv2.cvtColor(th2, cv2.COLOR_GRAY2BGR), "Otsu Gaussian filter")

### triangle 
gray_image_blurred = cv2.GaussianBlur(gray_image, (25, 25), 0)  #가우시안 필터링
start_time2 = time.time()
ret2, th2 = cv2.threshold(gray_image_blurred, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_TRIANGLE)
end_time2 = time.time()

print("triangle's time : ", end_time2 - start_time2)
show_with_matplotlib(cv2.cvtColor(th2, cv2.COLOR_GRAY2BGR), "triangle Gaussian filter")

#해당 예시에서는 통계적 접근 방법을 사용하는 otsu가 기하적 접근 방법을 사용하는 triangle보다 수행시간이
#조금 더 빠르다.